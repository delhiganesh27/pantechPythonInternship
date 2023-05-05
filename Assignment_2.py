import random
import time
from playsound import playsound
TEM_THRESHOLD = 30
HUM_THRESHOLD = 80


def value_gen():
    temperature = random.uniform(20, 50)
    humidity = random.uniform(40, 100)
    return temperature, humidity


while True:
    temp, hum = value_gen()
    print(temp, hum, "\n")
    if temp > TEM_THRESHOLD:
        print("Temperature Alarm Triggerred")
        playsound("alarm.wav")
    if hum > HUM_THRESHOLD:
        print("Humidity alarm triggerred")
        playsound("alarm.wav")

#    time.sleep(1)
