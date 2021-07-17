import matplotlib.pyplot as plt
import numpy as np

vortices = input("Enter number of Vortices -> ")
Vort_x = np.zeros(int(vortices))
Vort_y = np.zeros(int(vortices))

for i in range(1, 4):
    x = input("Enter "+ i +"vortice X crdnt: ")
    y = input("Enter "+ i +"vortice Y crdnt: ")
    np.append(Vort_x, x)
    np.append(Vort_y, y)

  