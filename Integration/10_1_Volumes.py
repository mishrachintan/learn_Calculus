import matplotlib.pyplot as plt
import numpy as np
import sympy

# Plot x =y^2
fig = plt.figure()
az = fig.add_subplot(1,1,1,projection='3d')

up_lim = 3
lo_lim = 0
points = 10*(up_lim-lo_lim)

u = np.linspace(lo_lim, up_lim, points)
v = np.linspace(0, 2*np.pi, 60)
U, V = np.meshgrid(u, v)
Z = U

# function 1
func = Z**2 + 1
X1 = (func)*np.cos(V)
Y1 = (func)*np.sin(V)

# function 2
func2 = 1
X2 = (func2)*np.cos(V)
Y2 = (func2)*np.sin(V)

az.plot_surface(X1, Y1, Z, alpha=0.3, color='blue')
az.plot_surface(X2, Y2, Z, alpha=0.2, color='green')

# Calculate volume of inner region between func1 and func2
x, y = sympy.symbols('x y')
out_radius = y**2 + 1
out_area = sympy.pi*out_radius**2
out_vol = sympy.integrate(out_area, (y, lo_lim, up_lim))

in_radius = 1
in_area = sympy.pi*in_radius**2
in_vol = sympy.integrate(in_area, (y, lo_lim, up_lim))

fin_vol = out_vol-in_vol

print(f"Area between the shapes: {out_vol}(out_vol)-{in_vol}(in_vol)={fin_vol}")

plt.show(block=False)
plt.pause(3)
plt.close()