from flask import Blueprint, request
from flask_cors import cross_origin
from controllers.predict_controller import predict_image

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST', 'OPTIONS'])
@cross_origin(origin='*', methods=['POST', 'OPTIONS'], allow_headers=['Content-Type', 'Authorization'])
def predict():
    if request.method == 'OPTIONS':
        return '', 204
    return predict_image()