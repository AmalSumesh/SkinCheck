from flask import Flask, request, make_response, jsonify
from routes.predict_routes import predict_bp

ALLOWED_ORIGIN = "*"  # allow any origin; switch to specific domain for production

app = Flask(__name__)

@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = make_response("", 204)
        response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.headers["Access-Control-Max-Age"] = "86400"
        return response

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization, X-Requested-With"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response

@app.errorhandler(Exception)
def handle_error(error):
    print(f"[ERROR] {str(error)}")
    response = jsonify({"error": str(error)})
    response.status_code = 500
    return response, 500

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
