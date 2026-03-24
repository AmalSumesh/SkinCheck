from flask import request, jsonify
from model.model_loader import model
from utils.preprocess import preprocess_image
from utils.gradcam import get_gradcam, overlay_gradcam
from utils.diagnosis_explainer import generate_llm_explanation

import numpy as np
from PIL import Image
import base64
import cv2


def predict_image():
    try:
        file = request.files['image']

        img = Image.open(file).convert("RGB")
        img = img.resize((380, 380))
        img_np = np.array(img)

        img_array = preprocess_image(file)

        pred = model.predict(img_array)[0][0]

        heatmap = get_gradcam(model, img_array)
        gradcam_img = overlay_gradcam(img_np, heatmap)

        _, buffer = cv2.imencode('.jpg', gradcam_img)
        gradcam_base64 = base64.b64encode(buffer).decode('utf-8')

        threshold = 0.5

        if pred > threshold:
            label = "Malignant"
            confidence = float(pred)
        else:
            label = "Benign"
            confidence = float(1 - pred)

        explanation = generate_llm_explanation(pred, confidence, heatmap)

        return jsonify({
            "prediction": label,
            "confidence": confidence,
            "gradcam": gradcam_base64,
            "explanation": explanation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500