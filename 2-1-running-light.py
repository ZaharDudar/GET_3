import RPi.GPIO as GPIO
import time

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
leds = [2,3,4,17,27,22,10,9]
GPIO.setup(leds,GPIO.OUT,pull_up_down=GPIO.PUD_OFF)

def turn_down_leds():
    GPIO.output(leds,0)
ind = 0

while(True):
    if(ind>7): ind = 0
    turn_down_leds()
    GPIO.output(leds[ind], 1)
    ind+=1
    time.sleep(0.2)
# GPIO.output(4,1)
