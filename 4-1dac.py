import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
DAC = [8,11,7,1,0,5,12,6]
GPIO.setup(DAC,GPIO.OUT)
GPIO.output(DAC,0)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]

try:
    while(True):
        a = input()
        if a=='q':
            break
        
        try:
            a = int(a)
        except ValueError:
            print("Не целое число")
        else:
            if a<0:
                print("Меньше 0")
            elif a>255:
                print("Больше 255")
            else:
                GPIO.output(DAC,dec2bin(a))
                print("{:.4f} V".format(a/256*3.3))
finally:
    GPIO.output(DAC,0)
    GPIO.cleanup()


