import RPi.GPIO as GPIO
import time
import signal
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT) #Red led at pin 9
GPIO.setup(10, GPIO.OUT) #Amber led at pin 10
GPIO.setup(11, GPIO.OUT) #Green led at pin 11
while True:
 # Red
 GPIO.output(9, True)
 time.sleep(3)
 # Red and amber
 GPIO.output(10, True)
 time.sleep(1)
 # Green
 GPIO.output(9, False)
 GPIO.output(10, False)
 GPIO.output(11, True)
 time.sleep(5)
 # Amber
 GPIO.output(11, False)
 GPIO.output(10, True)
 time.sleep(2)
 # Amber off (red comes on at top of loop)
 GPIO.output(10, False)
