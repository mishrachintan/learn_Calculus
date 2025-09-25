import sympy

x, y = sympy.symbols('x y')

eqn1 = sympy.sin(x)
print(f"Find the center of mass for {eqn1}, assume density=1")
lo_lim = 0
up_lim = sympy.pi


print(f"\t Step 1. calculate area under curve.")
mass = sympy.integrate(eqn1, (x, lo_lim, up_lim))
print(f"\t\t Mass->{mass}")

print(f"\t Step 2. calculate moment Mx(measured from x-axis,(bottom to top)).")
eqn_mx = eqn1*eqn1/2
mx = sympy.integrate(eqn_mx, (x, lo_lim, up_lim))
print(f"\t\t Mx->{mx}")

print(f"\t Step 3. calculate moment My(measured from y-axis,(left to right)).")
eqn_my = eqn1*x
my = sympy.integrate(eqn_my, (x, lo_lim, up_lim))
print(f"\t\t My->{my}")

print(f"\t Step 4. calculate x,y coordinate(x=My/M, y=Mx/M).")
x_center = my/mass
y_center = mx/mass
print(f"\t\t (x=My/M, y=Mx/M)->{x_center,y_center} OR {sympy.N(x_center),sympy.N(y_center)}")

# plot the center of mass point in graph
sympy.plot(eqn1, (x, 0, sympy.pi), markers=[{'args':[x_center, y_center, 'go']}])