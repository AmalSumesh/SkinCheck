from flask import Blueprint
from controllers.predict_controller import predict_image

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    return predict_image()