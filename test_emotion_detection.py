import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am happy")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        result = emotion_detector("I am very angry")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_sadness(self):
        result = emotion_detector("I feel very sad")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()