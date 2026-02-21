import requests
import json

def emotion_detector(text_to_analyse):
    # Handle blank/empty input
    if not text_to_analyse or text_to_analyse.strip() == "":
        return {
            'dominant_emotion': None,
            'scores': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    try:
        response = requests.post(url, json=myobj, headers=headers)
        
        # Check status_code 400 (Bad Request)
        if response.status_code == 400:
            return {
                'dominant_emotion': None,
                'scores': {
                    'anger': None,
                    'disgust': None,
                    'fear': None,
                    'joy': None,
                    'sadness': None
                }
            }
        
        # Parse successful response
        emotion_data = json.loads(response.text)
        emotions = emotion_data['emotionPredictions'][0]['emotion']
        
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
    
    except Exception:
        # Fallback for any other errors
        return {
            'dominant_emotion': None,
            'scores': {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None
            }
        }
