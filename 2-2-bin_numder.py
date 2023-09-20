import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time


GPIO.setmode(GPIO.BCM)
DAC = [8,11,7,1,0,5,12,6]
GPIO.setup(DAC,GPIO.OUT,pull_up_down=GPIO.PUD_OFF)
x,y = [],[]
GPIO.output(DAC,0)

# for i in range(0,256,):
for i in [0,5,32,64,127,255]:
    bin_num = bin(i)[2:]
    bin_num = '0'*(8-len(bin_num)) + bin_num
    print(bin_num)
    for ind in range(len(DAC)):
        GPIO.output(DAC[ind],int(bin_num[ind]))

    cur_v = int(input())
    y.append(cur_v)
    x.append(i)


GPIO.output(DAC,0)
GPIO.cleanup()
plt.plot(x,y,'bo')
plt.show()

