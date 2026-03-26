import os
os.environ["OMP_NUM_THREADS"] = "1"
import tensorflow as tf
tf.config.threading.set_intra_op_parallelism_threads(1)
tf.config.threading.set_inter_op_parallelism_threads(1)

from flask import Flask, jsonify
from flask_cors import CORS
from routes.predict_routes import predict_bp
from model.model_loader import get_model

app = Flask(__name__)

CORS(app)

print("[STARTUP] Warming up model...")
get_model()
print("[STARTUP] Model ready.")

@app.route("/health", methods=["GET"])
def health():
    return {"status": "healthy"}, 200

@app.route("/", methods=["GET"])
def home():
    return {
        "status": "API is running",
        "message": "Skin Cancer Classification Backend"
    }

app.register_blueprint(predict_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)