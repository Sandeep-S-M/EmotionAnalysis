from flask import Flask, render_template, request, jsonify
from EmotionDetection import emotion_detector
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST', 'GET'])
def emotionDetector():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text', '') if data else ''
    elif request.method == 'GET':
        text = request.args.get('textToAnalyze', '')
    
    if not text or text.strip() == "":
        return jsonify({
            'dominant_emotion': 'Invalid text! Please try again!',
            'scores': {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }
        })
    
    result = emotion_detector(text)
    
    if result['dominant_emotion'] is None:
        return jsonify({
            'dominant_emotion': 'Invalid text! Please try again!',
            'scores': {
                'anger': 0.0,
                'disgust': 0.0,
                'fear': 0.0,
                'joy': 0.0,
                'sadness': 0.0
            }
        }) 
    
    return jsonify({
        'dominant_emotion': result['dominant_emotion'],
        'scores': result['scores']
    })

    return jsonify(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
