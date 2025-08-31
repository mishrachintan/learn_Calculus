import sympy
import numpy as np

st = """===============================================================
    EXAMPLE 1: Calculate the area under the curve
===============================================================
"""
print(st)
x, y = sympy.symbols('x y')

y = sympy.sin(x)**3
print(f"equation: y={y}")

# find the zeroes of the equation
zeroes = sympy.solve(y)
print(f"Solving the eqauation: {zeroes}")

# calculate the total area
print(f"We want to find the total area in [0,2*pi], hence:")
print(f"\t However, sympy.integrate(y, (x, 0, 2*sympy.pi) -> {sympy.integrate(y, (x, 0, 2*sympy.pi))}")

area_1 = abs(sympy.integrate(y, (x, 0, sympy.pi)))
area_2 = abs(sympy.integrate(y, (x, sympy.pi, 2*sympy.pi)))
tot_area = area_1 + area_2
print(f"\t So, in order to fix this we have to find area as so:"
      f"\n\t sympy.integrate(y, (x, 0, {sympy.pi})))-> {area_1}"
      f"\n\t sympy.integrate(y, (x, {sympy.pi}, {2*sympy.pi})))-> {area_2}"
      f"\n\t\tabs(area[0, {sympy.pi}]) + abs(area[{sympy.pi}, {2*sympy.pi}]) -> {tot_area}")

# plot the equation
label = str((zeroes[0], 0))+"and"+str((zeroes[1], 0))
sympy.plot(y, label="sin(x)^3",
           #markers=[{'args': [[zeroes[0], zeroes[1]], [0, 0], 'r*'], 'ms': 20}],
           markers=[{'args': [[zeroes[0], zeroes[1]], [0, 0], 'go'], "label":label}],
           legend=True)

st2 = """\n===============================================================
    EXAMPLE 2: Calculate area between 2 curves
===============================================================
"""
print(st2)

x, y = sympy.symbols('x y')

curv_1 = x**2
curv_2 = x

print(f"Curve equations are:\n\t 1. {curv_1}\n\t 2. {curv_2}")

# find the ponts of intesection between these curves
roots = sympy.solve(sympy.Eq(curv_1, curv_2), x)
y1 = curv_2.subs(x, roots[0])
y2 = curv_2.subs(x, roots[1])
print(f"Solving for x->{roots}, \n\thence (x1,y1)->({roots[0]},{y1}); (x2,y2)->({roots[1]},{y2})")

# find the area between the curves for x:[0,1]
ar_1 = sympy.integrate(curv_1, (x, roots[0], roots[1]))
ar_2 = sympy.integrate(curv_2, (x, roots[0], roots[1]))
area_bet_curves = abs(ar_2-ar_1)
print(f"ar_1={ar_1}, ar_2={ar_2}, hence: \nArea between curves->abs(ar_2 - ar_1)={area_bet_curves}")

# plot the graphs
sympy.plot(curv_1, curv_2, (x, -1, 1.5))