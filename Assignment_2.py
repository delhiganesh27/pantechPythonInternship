import random    # for generating values
import time
import winsound  # for buzzer sound

'''Define the threshold level for temperature and humidity'''
TEM_THRESHOLD = 30
HUM_THRESHOLD = 70

'''Define a function for generation of temperature and humidity values'''


def value_gen():
    # generate temperature between 20 to 50 degree celsius
    temperature = random.uniform(20, 60)
    # generate humidity between 40% to 90%
    humidity = random.uniform(40, 90)
    return temperature, humidity


# Loop to generate values and check for alarms
while True:
    temp, hum = value_gen()
    print(f'Temperature : {temp:.2f} || Humidity : {hum:.2f}')
    '''Check for temperature and humidity alarms'''
    if temp > TEM_THRESHOLD:
        print("Temperature Alarm Triggered!!!")
        winsound.Beep(3150, 2000)  # generate buzzer sound for 2 seconds
    if hum > HUM_THRESHOLD:
        print("Humidity Alarm Triggered!!!")
        winsound.Beep(3150, 2000)  # generate buzzer sound for 2seconds
    print("\n")
    # wait for some time before generating the value
    time.sleep(2)
