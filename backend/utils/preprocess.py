from PIL import Image
import numpy as np
from tensorflow.keras.applications.efficientnet import preprocess_input

def preprocess_image(file):
    img = Image.open(file).convert("RGB")
    img = img.resize((380, 380))
    img_array = np.array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array