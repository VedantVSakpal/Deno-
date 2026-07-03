import unittest
from unittest.mock import patch

import speech


class SpeechTests(unittest.TestCase):
    def test_speak_returns_false_when_tts_is_unavailable(self):
        with patch("speech._create_tts_engine", return_value=None):
            self.assertFalse(speech.speak("hello"))

    def test_listen_returns_empty_string_when_recognition_is_unavailable(self):
        with patch("speech._create_recognizer", return_value=None):
            self.assertEqual(speech.listen(), "")


if __name__ == "__main__":
    unittest.main()
