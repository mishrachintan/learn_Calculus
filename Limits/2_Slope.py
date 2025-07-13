import matplotlib.pyplot as plt
import numpy as np
###from sympy.plotting import plot #sympy also has an plotting option

# For derivatives
import sympy
from sympy import symbols


# SLOPE FOR y=x**2
x = np.linspace(-10, 10, 50)  # 50 vales within -10,10
y = x**2

# first point
x1 = 1
y1 = x1**2

# second point
h = 1
x2 = 1+h
y2 = (x2)**2

rang = 10
x_pos_range = x1 + rang
x_neg_range = x1 - rang
y_pos_range = y1 + rang
y_neg_range = y1 - rang

plt.plot(x, y, color='magenta')
plt.plot(x1, y1, 'go')
plt.plot(x2, y2, 'go')
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.axis([x_neg_range,x_pos_range,y_neg_range,y_pos_range])
plt.grid(linestyle='--',linewidth=0.5)
plt.axhline(y=0, color='black') # draw a horizontal line
plt.axvline(x=0, color='black') # draw a verrical line
plt.show()


# Try to reduce the value of 'h' to get the slope of a point
#  the smaller the 'h' value, the better the approximation
#  we will try this with x**3 and see
x_val = 2
y_val = x_val**3

for i in range(1,11):
    h = 10**-i
    y_val_1 = (x_val+h)**3
    slope = (y_val_1-y_val)/h
    print(f"for h={h}, Slope={slope}")

