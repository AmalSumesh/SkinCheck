from tensorflow.keras.models import load_model as _load_model

_model = None

def get_model():
    global _model
    if _model is None:
        print("[MODEL] Loading model...")
        _model = _load_model("model/best_model.keras", compile=False)
        print("[MODEL] Model loaded successfully.")
    return _model