import pyttsx3
import speech_recognition as sr

class VoiceInterface:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.mic = sr.Microphone()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.mic as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
        try:
            command = self.recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I did not catch that."
        except sr.RequestError:
            return "API unavailable."
