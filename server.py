"""
Flask application for Emotion Detection API.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template('index.html')
@app.route("/emotionDetector")
def emo_analyzer():
    """Analyze the given text and return detected emotions."""
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "Error: No text provided.", 200
    response =emotion_detector(text_to_analyze)
    if "error" in response:
        return response["error"], 200
    if response is None or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 200
    text_response = (
        f"For the given statement, the system response is:\n"
        f"Anger: {response['anger']}\n"
        f"Disgust: {response['disgust']}\n"
        f"Fear: {response['fear']}\n"
        f"Joy: {response['joy']}\n"
        f"Sadness: {response['sadness']}\n"
        f"The dominant emotion is: {response['dominant_emotion']}"
    )
    return text_response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
