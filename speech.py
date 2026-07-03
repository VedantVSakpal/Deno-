import os


def _create_tts_engine():
    try:
        import pyttsx3  # type: ignore
    except Exception:
        return None

    try:
        return pyttsx3.init()
    except Exception:
        return None


def _create_recognizer():
    try:
        import speech_recognition as sr  # type: ignore
    except Exception:
        return None

    try:
        recognizer = sr.Recognizer()
        return recognizer
    except Exception:
        return None


def speak(text: str) -> bool:
    if not text:
        return False

    engine = _create_tts_engine()
    if engine is None:
        return False

    try:
        engine.say(text)
        engine.runAndWait()
        return True
    except Exception:
        return False


def listen() -> str:
    recognizer = _create_recognizer()
    if recognizer is None:
        return ""

    try:
        import speech_recognition as sr  # type: ignore

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        return recognizer.recognize_google(audio)
    except Exception:
        return ""
