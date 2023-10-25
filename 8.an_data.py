import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import json

fig, ax = plt.subplots(figsize=(10,7),dpi=100)

with open("lmsData/data.txt",'r') as f:
    data=np.array([int(i.strip()) for i in f.readlines()])

with open("lmsData/settings.json",'r') as f:
    settings = json.load(f)


data_volts=data*settings["step adc"]
t=np.arange(len(data))*settings["sampling rate"]


ax.plot(t,data_volts,"o-",markevery=30,label="V(t)")
ax.set_ylim([0,max(data_volts)+0.2])
ax.set_xlim([0,int(max(t))+1])

ax.text(6,2.3, f"Время зарядки {round(np.argmax(data_volts)*settings['sampling rate'],2)} c",wrap=True)
ax.text(6,2, f"Время разряда {round((len(data)-np.argmax(data_volts))*settings['sampling rate'],2)} c",wrap=True)

ax.set_ylabel("Напряжение на конденсаторе (В)")
ax.set_xlabel("Время (c)")
ax.grid(which='major',linestyle="-")
ax.grid(which='minor',linestyle="--")
ax.yaxis.set_minor_locator(tick.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(tick.MultipleLocator(0.5))

ax.set_title("Зависимость напряжения конденсатора от времени зарядки")
ax.legend()
fig.savefig("myPlot.svg")
plt.show()