import random
from time import sleep
while(1):
    temp = random.randint(1,100)
    humidity = random.randint(1,100)
    print("\nTemperature : {0} \nHumidity : {1}".format(temp,humidity))
    if(temp>50 and humidity < 50): 
        print("Alarm Detected")
    else:
        print("Alarm not detected")
    sleep(3)
