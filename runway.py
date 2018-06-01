import numpy as np
import matplotlib.pyplot as plt
from math import *

runwayxl = 'runway.csv'

runway = np.genfromtxt(runwayxl, dtype='string', delimiter=';')

y = []
x = []

for i in range(len(runway)):
    y.append(eval(runway[i][1].replace(',','.')))
    x.append(eval(runway[i][2].replace(',','.')))

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 14}

ax = plt.subplot(111)
box = ax.get_position()
plt.rc('font', **font)
plt.axis((0,100,0,4500))
plt.plot(x,y, label="runway length")
a=[[31.45,2275]]
plt.plot(*zip(*a), marker='o', markersize=8, color='fuchsia', label="reference aircraft") #A321neo
b=[[34.15,2320]]
plt.plot(*zip(*b), marker='o', markersize=8, color='fuchsia') #A321neo
ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.xlabel("% of airports")
plt.ylabel("runway length [m]")
plt.axhline(2000, linestyle="dashed", color="Red")
plt.axvline(23.73, linestyle="dashed", color="Red")
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid()
plt.show()
