import numpy as np
import matplotlib.pyplot as plt
import sympy
import mpl_toolkits.mplot3d.axes3d as axes3d

lo_limit = 0
up_limit = 3

fig = plt.figure()
# refer https://www.statology.org/fig-add-subplot/ for clarity on add_subplot
ax = fig.add_subplot(1, 1, 1, projection='3d')
points = 10*(up_limit-lo_limit)
u = np.linspace(lo_limit, up_limit, points)
v = np.linspace(0, 2*np.pi, 60)
U,V = np.meshgrid(u,v)
X = U

# define the function, think of U as "x" and V as "y"
#   and plot the graph
func = U**2
Y1 = (func)*np.cos(V)
Z1 = (func)*np.sin(V)
ax.plot_surface(X, Y1, Z1, alpha=0.4, color='blue')
plt.show(block=False)
plt.pause(2)
plt.close()

# Calulating the volume of the graph rotating about the x-axis
x, y = sympy.symbols('x y')
y = x**2
vol_expr = sympy.pi*y**2
vol = sympy.integrate(vol_expr, (x, 0, 3))
print(f"Volume of y=x^2, revolved around x-axis:")
print(f"\t Volume={vol}, sympy.N(vol)={sympy.N(vol)}")

#===========================================================================
# Plot a loudspeaker looking object
#===========================================================================
#  NOTE!!! Repeating the same as above for practice

#   set up the graph
figu = plt.figure()
axu = figu.add_subplot(1, 1, 1, projection='3d')
#points = 10*(up_limit-lo_limit)
uu = np.linspace(lo_limit, up_limit, points)
vu = np.linspace(0, 2*np.pi, 60)
UU,VU = np.meshgrid(uu,vu)
X1 = UU

#   define function1
func1 = UU**2 + 2
Y11 = (func1)*np.cos(VU)
Z11 = (func1)*np.sin(VU)

#   define function2
func2 = 2
Y22 = func2*np.cos(VU)
Z22 = func2*np.sin(VU)

axu.plot_surface(X1, Y11, Z11, alpha=0.3, color='blue')
axu.plot_surface(X1, Y22, Z22, alpha=0.2, color='red')

# Calculating volume of Object hollow at the center
outer_radius= (x**2)+2
vol_expr = sympy.integrate(sympy.pi*outer_radius**2, (x, 0, 3))

inner_radius = 2 # y=2 rotated around the x-axis
vol_hollo = sympy.integrate(sympy.pi*inner_radius**2, (x, 0, 3))

print(f"Volume of hollow object:")
print(f"\t Volume of y=(x^2)+2, revolved around x-axis - Volume of y=1, revolved around x-axis:")
final_vol = vol_expr-vol_hollo
print(f"\t\t{vol_expr}-{vol_hollo}={final_vol} or {sympy.N(final_vol, n=2)}")

plt.show(block=False)
plt.pause(5)
plt.close()




