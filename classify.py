from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np

# Load the trained model
model = load_model("models/best_model.keras")

# Load class names from fruit_labels.txt
with open("models/fruit_labels.txt", "r") as f:
    class_names = [line.strip() for line in f.readlines()]

def classify_image(image_path):
    try:
        # Load and preprocess the image
        img = load_img(image_path, target_size=(224, 224))  # same as Colab
        img = img_to_array(img)                             # converts to numpy array
        img = np.expand_dims(img, axis=0)                   # adds batch dimension

        # Predict
        prediction = model.predict(img)[0]                  # get first (only) result
        predicted_index = np.argmax(prediction) 
        predicted_label = class_names[predicted_index]
        confidence = prediction[predicted_index] * 100

        return f"{predicted_label} ({confidence:.2f}%)"

    except Exception as e:
        print(f"❌ Error processing image: {e}")
        return "Error"
 