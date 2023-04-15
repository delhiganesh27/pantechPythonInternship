import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Calibrating...")
        r.adjust_for_ambient_noise(source, duration=2)
        print("listening....")
        voice = r.listen(source)
        print("Recognizing...")
        text = r.recognize_google(voice)
        print(text)
        engine = pyttsx3.init()
        engine.say(text.lower())
        engine.runAndWait()

except sr.RequestError as e:
    print("Error: {0}".format(e))
