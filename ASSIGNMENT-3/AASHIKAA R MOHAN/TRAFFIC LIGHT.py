Import RPi.GPIO as GPIO
Import time
LED = 40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT)
While True:
 GPIO.output(LED,GPIO.HIGH)
 Time.sleep(1)
 GPIO.output(LED,GPIO.LOW)
 Time.sleep(1)
//Code for Traffic Light System//
From gpiozero import Button, TrafficLights, Buzzer
From time import sleep
Buzzer = Buzzer(15)
Button = Button(21)
Lights = TrafficLights(25, 8, 7)
While True:
 Button.wait_for_press()
 Buzzer.on()
 Light.green.on()
 Sleep(1)
 Lights.amber.on()
 Sleep(1)
 Lights.red.on()
 Sleep(1)
 Lights.off()
 Buzzer.off()
