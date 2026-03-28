from flask import request, jsonify
from model.model_loader import get_model
from utils.preprocess import preprocess_image
from utils.gradcam import get_gradcam, overlay_gradcam
from utils.diagnosis_explainer import generate_llm_explanation

from PIL import Image
import numpy as np
import cv2
import base64
import gc


def explain_image():
    try:
        file = request.files['image']

        img = Image.open(file).convert("RGB")
        img = img.resize((380, 380))
        img_np = np.array(img)

        file.seek(0)
        img_array = preprocess_image(file)

        model = get_model()


        heatmap = get_gradcam(model, img_array)

        gradcam_img = overlay_gradcam(img_np, heatmap)

        _, buffer = cv2.imencode('.jpg', gradcam_img)
        gradcam_base64 = base64.b64encode(buffer).decode('utf-8')

        model = get_model()
        pred = model.predict(img_array)[0][0]

        threshold = 0.5
        if pred > threshold:
            label = "Malignant"
            confidence = float(pred)
        else:
            label = "Benign"
            confidence = float(1 - pred)


        try:
            explanation = generate_llm_explanation(label, confidence, heatmap)
        except:
            explanation = "Explanation unavailable"

        del img_array, img_np, heatmap, gradcam_img
        gc.collect()

        return jsonify({
            "gradcam": gradcam_base64,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500