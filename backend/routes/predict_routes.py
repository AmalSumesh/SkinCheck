from flask import Blueprint, request
from controllers.predict_controller import predict_image

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return '', 204
    return predict_image()