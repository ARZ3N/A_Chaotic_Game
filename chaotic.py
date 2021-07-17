import matplotlib.pyplot as plt
import numpy as np
import random
from time import sleep
from matplotlib.animation import FuncAnimation

fig = plt.subplots()
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
    mid_x = (Vort_x[rdindex] + init_x)/2.0
    mid_y = (Vort_y[rdindex] + init_y)/2.0
    plt.scatter(Vort_x, Vort_y, c='g')
    plt.scatter(mid_x, mid_y, c='y')
    #sleep(0.5)

ani = FuncAnimation(plt.gcf, rt_plot, interval=500)
plt.tight_layout()
plt.show()