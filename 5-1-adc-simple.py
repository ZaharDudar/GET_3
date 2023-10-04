import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = [8,11,7,1,0,5,12,6]
comp=14
troyka=13
GPIO.setup(DAC,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=1)
GPIO.setup(comp,GPIO.IN)
GPIO.output(DAC,0)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]
    
def s_adc():
    for v in range(256):
        GPIO.output(DAC,dec2bin(v))
        time.sleep(0.005)
        if GPIO.input(comp)==1:
            return v

try:
    while(True):
        print("{:.2f}V".format(s_adc()/255 * 3.3))

finally:
    GPIO.output(DAC,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()