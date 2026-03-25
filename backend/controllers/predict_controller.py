from flask import request, jsonify
from model.model_loader import get_model
from utils.preprocess import preprocess_image
from utils.gradcam import get_gradcam, overlay_gradcam
from utils.diagnosis_explainer import generate_llm_explanation

import numpy as np
from PIL import Image
import base64
import cv2
import gc
import traceback


def predict_image():
    try:
        file = request.files['image']

        img = Image.open(file).convert("RGB")
        img = img.resize((380, 380))
        img_np = np.array(img)

        file.seek(0)
        img_array = preprocess_image(file)

        model = get_model()
        pred = model.predict(img_array)[0][0]

        # Run GradCAM, then immediately free tensors to recover RAM
        heatmap = get_gradcam(model, img_array)
        del img_array
        gc.collect()

        gradcam_img = overlay_gradcam(img_np, heatmap)
        del img_np
        gc.collect()

        _, buffer = cv2.imencode('.jpg', gradcam_img)
        gradcam_base64 = base64.b64encode(buffer).decode('utf-8')
        del gradcam_img, buffer
        gc.collect()

        threshold = 0.5
        if pred > threshold:
            label = "Malignant"
            confidence = float(pred)
        else:
            label = "Benign"
            confidence = float(1 - pred)

        # LLM call after heavy memory is freed
        explanation = generate_llm_explanation(pred, confidence, heatmap)
        del heatmap
        gc.collect()

        return jsonify({
            "prediction": label,
            "confidence": confidence,
            "gradcam": gradcam_base64,
            "explanation": explanation
        })

    except Exception as e:
        tb = traceback.format_exc()
        print("[PREDICT ERROR]", str(e))
        print(tb)
        return jsonify({"error": "Internal server error", "detail": str(e)}), 500

    except Exception as e:
        print(f"[PREDICT ERROR] {e}")
        return jsonify({"error": str(e)}), 500