import speech_recognition as sr
import pyttsx3
import pandas as pd


class audio:

    def audioOut(self, text):
        print(text.capitalize())
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 130)
        engine.say(text.lower())
        engine.runAndWait()

    def audioIn(self):
        recogn = sr.Recognizer()
        with sr.Microphone() as source:
            print("Calibrating...")
            recogn.adjust_for_ambient_noise(source, duration=2)
            self.audioOut("Tell the Operation you want to perform".lower())
            voice = recogn.listen(source)
        try:
            print("Recognizing...")
            text = recogn.recognize_google(voice, language="en-in")

        except sr.UnknownValueError:
            self.audioOut("Sorry,I  could not recognize what you said")
            self.audioOut("Please say again")
            return "None"
        except sr.RequestError:
            self.audioOut("Sorry,there was an error with recognizing service")
        print(text)
        return text


class data(audio):
    def __init__(self, file):
        self.file = file

    def action(self):
        dataset = pd.read_csv(file)
        while True:
            print('''
            1.Column names\n
            2.Occurrence of null value\n
            3.Shape\n
            4.Glance about dataset\n
            5.End''')

            operation = self.audioIn()
            if 'column' in operation:
                self.audioOut("The result of column names operation")
                print(dataset.columns)
            elif 'null value' in operation or 'check null' in operation:
                self.audioOut("The result of occurrence null value operation")
                print(dataset.isnull().sum())
            elif 'shape' in operation:
                self.audioOut(
                    f"The data set has {dataset.shape[0]} rows and {dataset.shape[1]} columns".lower())
            elif 'glance' in operation or 'sample' in operation:
                self.audioOut(f"The result of the sample operation".lower())
                print(dataset.head())
            elif 'end' in operation or 'stop' in operation or 'quit' in operation or 'exit' in operation:
                self.audioOut("Thanking for using us")
                break
            elif operation == "None":
                continue
            else:
                self.audioOut("Sorry Please tell a valid action".lower())
                continue
            print("-"*100)


file = input("Enter the file path : ")
user = data(file)
user.action()
