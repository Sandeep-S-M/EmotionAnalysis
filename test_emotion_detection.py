import unittest
from EmotionDetection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_joy_statement(self):
        """Test 'I am glad this happened' returns joy"""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')
    def test_anger_statement(self):
        """Test 'I am really mad about this' returns anger"""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')
    def test_disgust_statement(self):
        """Test 'I feel disgusted just hearing about this' returns disgust"""
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')
    def test_sadness_statement(self):
        """Test 'I am so sad about this' returns sadness"""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')
    def test_fear_statement(self):
        """Test 'I am really afraid that this will happen' returns fear"""
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')
    def test_blank_input(self):
    """Test blank input returns None values"""
        result = emotion_detector("")
        self.assertIsNone(result['dominant_emotion'])
        self.assertIsNone(result['scores']['joy'])
if __name__ == '__main__':
    unittest.main()
