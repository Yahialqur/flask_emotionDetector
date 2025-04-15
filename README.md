# 🧠 NLP Emotion Detection Web App

This is a simple web application that analyzes the emotional tone of input text using IBM Watson’s Natural Language Processing (NLP) Emotion Recognition API.

> ⚠️ **Note:** The IBM Watson API used in this project is currently **unavailable**. While the app code and interface remain functional, the API endpoint has been deprecated or is no longer accessible, so emotion detection will not return valid results.

---

## 🚀 Features

- Accepts user input via a web interface
- Sends text to IBM Watson NLP Emotion API
- Parses response to detect levels of:
  - **Anger**
  - **Disgust**
  - **Fear**
  - **Joy**
  - **Sadness**
- Displays the dominant emotion as output

---

## 💠 Tech Stack

- **Backend**: Python, Flask  
- **Frontend**: HTML, Bootstrap, JavaScript  
- **API**: IBM Watson NLP EmotionPredict (currently deprecated)

---

## 🖥️ How to Run

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd EmotionDetection
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask requests
   ```

4. Start the Flask server:
   ```bash
   python server.py
   ```

5. Open your browser and go to:
   ```
   http://localhost:5000
   ```

---

## 🧪 Run Unit Tests

To run the provided unit tests:
```bash
python test_emotion_detection.py
```

---

## 📌 Known Issues

- ❗️ **IBM Watson Emotion API** used in this project is no longer available.
- Emotion detection results will be unavailable unless the API is replaced or restored.

---

## 👤 Author

Created by Yahia Alqurnawi as a personal NLP mini-project.
