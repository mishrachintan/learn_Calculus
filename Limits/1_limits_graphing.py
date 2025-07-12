# Source: College calculus-Full course with python code [freecodecamp youtube]

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,100)
y = (3*x**2)/(x**2-4)

x_min = y_min = -10
x_max = y_max = 10

plt.plot(x, y, color='magenta', label='t')
plt.axis([x_min,x_max,y_min,y_max])
plt.xlabel("x-value")
plt.ylabel("y-value")
plt.grid(linestyle='--',linewidth=0.5)
plt.axhline(y=0, color='black') # draw a horizontal line
plt.axvline(x=0, color='black') # draw a verrical line
plt.title("Graph of y = (3*x**2)/(x**2-4)")
plt.show()
