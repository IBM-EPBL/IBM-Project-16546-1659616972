import random
from time import sleep
start1=int(input("temp start value:"))
end1=int(input("temp nd value:"))
start2=int(input("humidity start value:"))
end2=int(input("humidity end value:"))
while(1):
    temp=random.randint(start1,end1)
    humi=random.randint(start2,end2)
    print("\ntemperature={0}  \nhumidity= {1}".format(temp,humi))
    if(humi < 30 and temp>45):
        print("Alarm Detecetd!!!!")
    else:
        print("No problem")
    sleep(5)
