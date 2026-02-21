import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj =  { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=headers)
    emotion_store = json.loads( response.text)

    emotions = emotion_store['emotionPredictions'][0]['emotion']
    required_emotions = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'], 
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    dominant_emotion = max(required_emotions, key=required_emotions.get)
    
    return {
        'dominant_emotion': dominant_emotion,
        'scores': required_emotions
    }
    