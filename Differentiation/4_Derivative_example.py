import sympy

# Enter the equation
x, y = sympy.symbols('x y')
y = x**3 - 9*x**2 + 24
print(f"y = {y}")
print("=========================================================")

# Find the first derivative
f_derv = sympy.diff(y, x)
print(f"First derivative: {f_derv}")
print(f"Derivative at x = 2: {f_derv.subs(x, 2)}")
print(f"Points of change(local maximum/ local minimum):")
f_solve = sympy.Eq(f_derv, 0)
f_roots = sympy.solve(f_solve)
print(f"\t Make 1st derv equal to 0: {f_derv}=0. \n\t Roots={f_roots}")
print("Calculating 'y' values for the respective x maxima/minima:")
for i in f_roots:
    t = y.subs(x, i)
    print(f"\t ({i},{t})")
print("=============================================================")

# Find the second derivative
print("Second derivative gives the change of slope or inflection")
f2_derv = sympy.diff(f_derv, x)
print(f"\t {f2_derv}")
print(f"Solving for {f2_derv}=0")
f2_solve = sympy.Eq(f2_derv, 0)
f2_roots = sympy.solve(f2_solve)
print(f"\t 2nd derivative roots = {f2_roots}")
for i in f2_roots:
    print(f"\t Point of inflection: ({i},{f_derv.subs(x, i)})")

# Plot the equations
sympy.plot(y,f_derv,f2_derv, ylim=[-100,100], legend=True)
