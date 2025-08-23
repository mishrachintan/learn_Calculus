import math
import sympy
import matplotlib.pyplot as plt
from sympy import plot_parametric

##NOTE: Also check tangent line equations
x,y,t = sympy.symbols('x y t')

y = sympy.sin(t)
x = sympy.cos(t)
##############################
# Method 1 plotting
##############################
x_vals = []
y_vals = []

for i in range(36):
    v = math.pi * i/12
    y_vals.append(y.subs(t, v))
    x_vals.append(x.subs(t, v))

plt.plot(y_vals, x_vals)
plt.title("Matplotlib graph")
plt.show()

##############################
# Method 2 plotting
##############################
# plot x, y w.r.t 't' from 0 to 2*pi
plot_parametric(x, y, (t, 0, 2*sympy.pi))

# plot equation for sin(t)
plot_parametric(t, y, (t, 0, 4*sympy.pi))

# plot equation for cos(t)
plot_parametric(t, x)

# dy/dx = (dy/dt)/(dx/dt)
dydt = sympy.diff(y, t)
print(f"dy/dt = {dydt}")
dxdt = sympy.diff(x, t)
print(f"dx/dt = {dxdt}")
dydx = dydt/dxdt
print(f"dy/dx = {dydx}")

print("============================================")
print(f"Slope with math.pi is numerical {dydx.subs(t, math.pi/12)}")
print(f"Slope with sympy.pi is NOT numerical {dydx.subs(t, sympy.pi/12)}")
