import os
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import streamlit as st
from PIL import Image

# Load CSV file
music_mode_df = pd.read_csv(r'C:\Users\Ranjan kumar pradhan\.vscode\Music_Mood_predict\data_moods.csv')

# Load the pre-trained mood classification model
model = load_model(r'C:\Users\Ranjan kumar pradhan\.vscode\Music_Mood_predict\mood_classification_model.h5')

# Data Preprocessing
img_width, img_height = 150, 150

def preprocess_image(image):
    image = image.resize((img_width, img_height))
    image_array = np.array(image) / 255.0
    if image_array.ndim == 2:  # Grayscale image
        image_array = np.stack((image_array,) * 3, axis=-1)
    elif image_array.shape[-1] == 1:  # Single channel image
        image_array = np.repeat(image_array, 3, axis=-1)
    image_array = np.expand_dims(image_array, axis=0)
    return image_array
# Music Recommendation Engine
mood_to_music = {
    'Happy': music_mode_df[music_mode_df['mood'] == 'Happy'],
    'Sad': music_mode_df[music_mode_df['mood'] == 'Sad'],
    'Energetic': music_mode_df[music_mode_df['mood'] == 'Energetic'],
    'Calm': music_mode_df[music_mode_df['mood'] == 'Calm']
}

def map_model_mood_to_csv_mood(model_mood):
    mood_mapping = {
        'happy': 'Happy',
        'sad': 'Sad',
        'angry': 'Energetic',
        'disgust': 'Sad',
        'fear': 'Calm',
        'neutral': 'Calm',
        'surprise': 'Energetic'
    }
    return mood_mapping.get(model_mood.lower(), 'Calm')

def recommend_music(mood):
    recommendations = mood_to_music.get(mood, pd.DataFrame()).sample(n=1)
    for _, row in recommendations.iterrows():
        st.write(f"Recommended Music: {row['name']}, Album_name: {row['album']}, Artist_name: {row['artist']}")

# Streamlit App
def main():
    st.title("Mood for Music")
    st.write("Upload an image to detect your mood and get a music recommendation!")

    uploaded_file = st.file_uploader("Choose an image...")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_container_width=True)

        # Preprocess the image
        image_array = preprocess_image(image)

        # Predict mood
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)
        model_mood = list(mood_to_music.keys())[predicted_class[0]]
        mood = map_model_mood_to_csv_mood(model_mood)

        st.write(f"Detected Mood: {model_mood} (mapped to:{mood})")
        recommend_music(mood)

if __name__ == "__main__":
    main()
