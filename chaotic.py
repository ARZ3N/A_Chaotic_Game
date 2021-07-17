import matplotlib.pyplot as plt
import numpy as np
import random

vortices = input("Enter number of Vortices -> ")
Vort_x = np.zeros(int(vortices))
Vort_y = np.zeros(int(vortices))

for i in range(1, 4):
    x = input("Enter "+ i +"vortice X crdnt: ")
    y = input("Enter "+ i +"vortice Y crdnt: ")
    np.append(Vort_x, x)
    np.append(Vort_y, y)

init_x = input("Enter X crdnt of strtng pnt -> ")
init_y = input("Enter Y crdnt of strtng pnt -> ")

# a <= rand_int <= b : randrange(a, b+1)
def roll_dice(n_vortice):
    return random.randrange(1, n_vortice+1)

