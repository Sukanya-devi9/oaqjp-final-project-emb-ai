import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertIn('dominant_emotion', result_1, "Missing 'dominant_emotion' key in output")
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
unittest.main()