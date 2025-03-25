import requests
import json
def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj={ "raw_document": { "text": text_to_analyze } }
    response=requests.post(URL,json=myobj,headers=Headers)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    if response.status_code != 200:
        return {"error": "API request failed"}
    formatted_response = response.json()
    try:
        emotions=formatted_response['emotionPredictions'][0]['emotion']
    except (KeyError, IndexError):
        return {"error": "Invalid response structure"}
    required_emotions={key:emotions.get(key,0) for key in['anger','disgust','fear','joy','sadness']}
    dominant_emotion = max(required_emotions, key=required_emotions.get)
    required_emotions['dominant_emotion'] = dominant_emotion  
    return required_emotions

    


