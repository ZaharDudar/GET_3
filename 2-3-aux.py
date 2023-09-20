import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
aux_inp=[21,20,26,16,19,25,23,24]
leds = [2,3,4,17,27,22,10,9]

GPIO.setup(leds,GPIO.OUT)
GPIO.setup(aux_inp,GPIO.IN,pull_up_down=GPIO.PUD_UP)

try:
    while(True):
        for i in range(8):
            if(GPIO.input(aux_inp[i])==0):
                GPIO.output(leds[i],0)
            else:
                GPIO.output(leds[i],1)
except KeyboardInterrupt:
    GPIO.output(leds,0)
    GPIO.cleanup()