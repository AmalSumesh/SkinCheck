from flask import request, jsonify
from model.model_loader import get_model
from utils.preprocess import preprocess_image

from PIL import Image
import numpy as np


def predict_image():
    try:
        file = request.files['image']

        img = Image.open(file).convert("RGB")
        img = img.resize((380, 380))

        file.seek(0)
        img_array = preprocess_image(file)

        model = get_model()
        pred = model.predict(img_array)[0][0]

        threshold = 0.5
        if pred > threshold:
            label = "Malignant"
            confidence = float(pred)
        else:
            label = "Benign"
            confidence = float(1 - pred)

        return jsonify({
            "prediction": label,
            "confidence": confidence
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500