import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [2,3,4,17,27,22,10,9]
GPIO.setup(leds,GPIO.OUT)


for led in leds:
    GPIO.output(led,0)


GPIO.cleanup(leds)