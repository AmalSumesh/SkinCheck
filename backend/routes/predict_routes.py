from flask import Blueprint
from controllers.predict_controller import predict_image
from controllers.explain_controller import explain_image

predict_bp = Blueprint('predict', __name__)

predict_bp.route('/predict', methods=['POST'])(predict_image)
predict_bp.route('/explain', methods=['POST'])(explain_image)