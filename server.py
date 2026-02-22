"""
Server module for the Emotion Detector Flask application.
"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Display the home page with input form.
    """
    return (
        "<h2>Emotion Detector</h2>"
        '<form action="/emotionDetector" method="get">'
        '<input type="text" name="textToAnalyze" '
        'placeholder="Enter text here">'
        '<input type="submit" value="Analyze">'
        "</form>"
    )


@app.route("/emotionDetector")
def emotion_detection_route():
    """
    Process the emotion detection request.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid text! Please try again!"

    return (
        "<h3>Emotion Results:</h3>"
        f"Anger: {result['anger']}<br>"
        f"Disgust: {result['disgust']}<br>"
        f"Fear: {result['fear']}<br>"
        f"Joy: {result['joy']}<br>"
        f"Sadness: {result['sadness']}<br>"
        f"<b>Dominant Emotion: {result['dominant_emotion']}</b>"
    )


if __name__ == "__main__":
    app.run(debug=True)
