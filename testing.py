import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("mushroom_mobilenet_model.h5")

# Class labels and descriptions
class_info = {
     "Combine": {
        "advantage": "Can be used for multiple purposes, including culinary and medicinal. Offers flexibility in applications and research.",
        "disadvantage": "Requires careful identification to avoid confusion with toxic species. Misidentification may lead to health risks."
    },
    "Edible": {
        "advantage": "Safe for consumption, rich in nutrients and vitamins. Supports immune system and provides dietary benefits.",
        "disadvantage": "Overconsumption or allergic reactions could cause health issues. Some species may be edible only when properly cooked."
    },
    "object": {
        "advantage": "It's an object used to represent or hold classification data within the system.",
        "disadvantage": "It's an abstract placeholder and not a real mushroom type. May cause confusion if misinterpreted as a category."
    },
    "poisonus": {
        "advantage": "Helps in warning against dangerous mushrooms. Educates users to avoid harmful or life-threatening species.",
        "disadvantage": "Highly toxic; can cause severe health problems or death if ingested. Misidentification can be fatal."
    }
}

# Streamlit UI
st.title("🍄 Mushroom Classification ")
st.write("Upload an image of a mushroom to classify it.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load and preprocess the image
    img = Image.open(uploaded_file).convert("RGB")
    img_resized = img.resize((224, 224))  # Resize to match model input

    # Convert to array
    img_array = image.img_to_array(img_resized) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Make prediction
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = np.max(predictions)

    # Get class label
    class_labels = list(class_info.keys())
    predicted_label = class_labels[predicted_class]

    # Display Image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Display Prediction
    st.write(f"**Prediction:** {predicted_label}")  
    st.write(f"**Confidence:** {confidence:.2f}")

    # Display Advantage and Disadvantage
    st.subheader("Advantages and Disadvantages")
    st.write(f"**Advantage:** {class_info[predicted_label]['advantage']}")
    st.write(f"**Disadvantage:** {class_info[predicted_label]['disadvantage']}")
