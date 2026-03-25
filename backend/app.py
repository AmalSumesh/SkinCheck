from flask import Flask, request
from flask_cors import CORS
from routes.predict_routes import predict_bp

ALLOWED_ORIGIN = "https://skin-check-alpha.vercel.app"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ALLOWED_ORIGIN}})

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response

@app.route("/", methods=["GET"])
def home():
    return {
        "status": "API is running",
        "message": "Skin Cancer Classification Backend"
    }

app.register_blueprint(predict_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)