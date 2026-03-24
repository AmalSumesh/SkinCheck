from flask import Flask
from flask_cors import CORS
from routes.predict_routes import predict_bp

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(predict_bp)

if __name__ == "__main__":
    app.run(debug=True)