import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = [8,11,7,1,0,5,12,6]
GPIO.setup(DAC,GPIO.OUT)
GPIO.output(DAC,0)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
val =0
T=3
step=1
try:
    while(True):
        val+=step
        if val==255 or val ==0:
            step = -step
        GPIO.output(DAC,dec2bin(val))
        print(val)
        time.sleep(T/510)
finally:
    GPIO.output(DAC,0)
    GPIO.cleanup()