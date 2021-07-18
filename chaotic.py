import matplotlib.pyplot as plt
import numpy as np
import random
from time import sleep
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.style.use('fivethirtyeight')

vortices = int(input("Enter number of Vortices -> "))
Vort_x = np.zeros(int(vortices))
Vort_y = np.zeros(int(vortices))

for i in range(1, vortices+1):
    print('Enter X crdnt of vortice '+str(i)+' : ')
    x = input()
    print('Enter Y crdnt of vortice '+str(i)+' : ')
    y = input()
    np.append(Vort_x, x)
    np.append(Vort_y, y)

init_x = float(input("Enter X crdnt of strtng pnt -> "))
init_y = float(input("Enter Y crdnt of strtng pnt -> "))

# a <= rand_int <= b : randrange(a, b+1)
def roll_dice(n_vortice):
    return random.randrange(1, n_vortice+1)

def rt_plot(i):
    rdindex = roll_dice(vortices)
    mid_x = (Vort_x[rdindex-1] + init_x)/2.0
    mid_y = (Vort_y[rdindex-1] + init_y)/2.0
    ax1.scatter(Vort_x, Vort_y, c='g')
    ax1.scatter(mid_x, mid_y, c='y')


ani = animation.FuncAnimation(fig, rt_plot, interval=500)
plt.tight_layout()
plt.show()