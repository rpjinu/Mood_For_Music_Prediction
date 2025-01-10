# Mood_For_Music_Prediction
(An Intelligent Mood Detection and Music Recommendation Application)
# 🌟 Mood-Based Music Recommendation System 🌟

<img src="https://github.com/rpjinu/Mood_For_Music_Prediction/blob/main/project_image.png" width="600">
## 📊 Project Overview
This project is a 🎶 Mood-Based Music Recommendation System 🎶 that utilizes 💻 deep learning and 🖼️ image processing to detect a user's mood from a still 📸 image. Based on the detected mood, the system recommends a personalized 🎵 music track from a predefined dataset. The primary objective is to enhance the user's emotional experience by aligning 🎶 music with their current mood.

## 🔗 Features
- **😊 Mood Detection**: Utilizes a pre-trained 🤖 Convolutional Neural Network (CNN) model to detect the user's mood from an uploaded 📷 image.
- **🎵 Music Recommendation**: Recommends 🎶 music based on the detected mood using a predefined 🗃️ CSV dataset.
- **👨‍💻 User Interface**: Provides a user-friendly interface built with 🔊 Streamlit for uploading 📷 images and displaying mood and 🎶 music recommendations.

## 🔧 Tech Stack
- **💎 Python**: Core programming language.
- **💪 TensorFlow/Keras**: For loading the pre-trained mood classification model.
- **📈 Pandas**: For handling and processing the 🎵 music dataset.
- **🔊 Streamlit**: For building the 🌐 web interface.
- **🖼️ PIL**: For 📷 image processing.

## 🔧 Installation
### ⚙️ Prerequisites
- Python 3.7+
- 🔐 Virtual environment (optional but recommended)

### 🔄 Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mood-music-recommendation.git
   cd mood-music-recommendation
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Place the pre-trained model and 🗃️ CSV dataset in the appropriate directories:
   - `path_to/mood_classification_model.h5`
   - `path_to/MoodforMusic/music_mode.csv`

## 🔌 Usage
1. Run the 🔐 Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Upload an 📷 image through the interface.
3. View the detected mood and recommended 🎶 music based on the uploaded 📷 image.

## 🌐 Project Structure
```
.
├── app.py                     # Main application file
├── path_to/
│   ├── mood_classification_model.h5  # Pre-trained model
│   └── MoodforMusic/
│       └── music_mode.csv     # Music dataset
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## 🗃️ CSV Dataset Structure
The 📃️ CSV file `music_mode.csv` should have the following columns:
- `album`: Name of the 🎵 album
- `artist`: Name of the 🎤 artist
- `mood`: Mood of the 🎶 music track

Example:
```
album,artist,mood
1999,Prince,Happy
23,Blonde Redhead,Sad
9 Crimes,Damien Rice,Sad
99 Luftballons,Nena,Happy
...
```

## 🚀 Future Enhancements
- **🎥 Video Input Support**: Extend the system to accept 🎥 video inputs for dynamic mood detection.
- **😊 Expanded Mood Categories**: Include more nuanced mood categories for better recommendations.
- **👨‍💻 Enhanced UI/UX**: Improve the user interface for a more interactive experience.

## 👪 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 🗄️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👍 Acknowledgements
- The pre-trained model and dataset were instrumental in the development of this project.
- Thanks to the open-source community for providing valuable resources and tools.

