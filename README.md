# ToxiMushroom - Poisonus Mushroom Detection using CNN🍄
A deep learning-based web application for detecting poisonous mushrooms from images using Convolutional Neural Networks (CNN).

## 🚀 Project Overview
ToxiMushroom is a smart image classification system designed to help users determine whether a mushroom is **poisonous**,**edible**,**combination** **object** by simply 
uploading a photo. The model is trained using a custom dataset and is built with TensorFlow and CNN architectures.

## 🧠 Features
- 🔍 Detects if a mushroom is poisonous or edible using an image.
- 🧠 Trained using CNN (ResNet-based architecture).
- 📸 Accepts user image uploads for classification.
- 🧾 Displays detailed info for edible mushrooms.
- ☠️ Shows a warning sign for poisonous mushrooms.

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask / Python
- **Machine Learning**: TensorFlow, Keras, OpenCV
- **Tools**: Jupyter Notebook, Anaconda, VS Code

## 🖼️ Sample Prediction
Upload a mushroom image via the web UI:
- If *edible*: Display its name and uses.
- If *poisonous*: Show red warning sign and danger message.

## 📁 Project Structure
ToxiMushroom/
├── static/
├── templates/
│ ├── index.html
│ └── home.html
├── model/
│ └── mushroom_model.h5
├── app.py
├── training.ipynb
├── requirements.txt
└── README.md

## 📊 Dataset
-Collected over 70,000 mushroom images across 100 species

-Preprocessed for cap shape, color, and structure.

-Data Augmentation techniques used for better accuracy.

## ✅ Future Enhancements
-📱 Deploy as a mobile app

-🌍 Multi-language support

-🧬 Integrate with a mushroom species database for taxonomy info

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

