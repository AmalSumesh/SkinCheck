from flask import Flask
from flask_cors import CORS
from routes.predict_routes import predict_bp

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {
        "status": "API is running",
        "message": "Skin Cancer Classification Backend"
    }

app.register_blueprint(predict_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)