"""
Server for emotion detection application.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

# Create flask app named Emotion Detection
app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def detect_emotion():
    """
    Handle GET requests to /emotionDetector and return emotion analysis results.
    """
    # Get the text input from the query string (GET request)
    text_to_analyze = request.args.get('textToAnalyze')

    # Use the emotion detector function to analyze the text
    result = emotion_detector(text_to_analyze)

    # Error handling
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Construct a formatted response string
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    # Return the formatted response to be displayed on the page
    return response_text

# Route to render the index.html page
@app.route("/")
def render_index_page():
    """
    Render the index.html page.
    """
    return render_template("index.html")

# Run the server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    