import requests
import json

def emotion_detector(text_to_analyze):

     # URL of the sentiment analysis service
     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

     # Constructing the request payload in the expected format
     myobj = {"raw_document": {"text": text_to_analyze}}

     # Custom header specifying the model ID for the sentiment analysis service
     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

     # Sending a POST request to the sentiment analysis API
     response = requests.post(url, json=myobj, headers=header)

     # Convert response text into a dictionary using the json library
     response_dict = json.loads(response.text)

     # Extract the emotions from the nested response structure
     emotions = response_dict['emotionPredictions'][0]['emotion']

     # Extract individual emotion scores
     anger_score = emotions['anger']
     disgust_score = emotions['disgust']
     fear_score = emotions['fear']
     joy_score = emotions['joy']
     sadness_score = emotions['sadness']

     # Build a scores-only dict to find the dominant emotion
     scores = {
     'anger': anger_score,
     'disgust': disgust_score,
     'fear': fear_score,
     'joy': joy_score,
     'sadness': sadness_score
     }

     # Dominant emotion is the one with the highest score
     dominant_emotion = max(scores, key=scores.get)

     # Return the required output format
     return {
     'anger': anger_score,
     'disgust': disgust_score,
     'fear': fear_score,
     'joy': joy_score,
     'sadness': sadness_score,
     'dominant_emotion': dominant_emotion
     }
