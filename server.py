"""
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask web app
app = Flask("Emotion Detector")

# Python decorator to define specific URL endpoint
@app.route("/emotionDetector")
def emotion_detector_route():
    """
    This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the emotions and their
    confidence scores, along with the dominant emotion.
    """

    # Flask server captures input from the user's web browser
    text_to_analyze = request.args.get("textToAnalyze")

    # Sends captured input to the underlying AI model
    response = emotion_detector(text_to_analyze)

    # Check for invalid input (blank or unprocessable text)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # f-strings make the emotion values explicit
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

# Python decorator to define root or homepage of website
@app.route("/")
def render_index_page():
    """
    This function initiates the rendering of the main application
    page over the Flask channel.
    """
    return render_template('index.html')

# standard Python idiom that ensures the server if the script is run directly,
# rather than be imported as a module by another file
if __name__ == "__main__":
    # host="0.0.0.0" makes it accessible on your local network
    # port=5000 is the default Flask port
    app.run(host="0.0.0.0", port=5000)
