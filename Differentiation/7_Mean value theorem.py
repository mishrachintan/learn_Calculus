# Mean Value theorem
import sympy

print("======================================================================")
print("MEAN VALUE THEOREM:")
print(" If the function is continous on closed interval [a, b] and "
      "\n differentiable on an open interval (a,b) then there exists atleast"
      "\n one point c where f'(c) is equal to function's avg. rate of change"
      "\n over the entire interval [a, b]:"
      "\n\t   f'(c)=f(b)-f(a)/b-a")
print("======================================================================")

x, y = sympy.symbols('x y')

expr = x**3+5*x**2-3*x+20

x1 = -7
x2 = 3

y1 = expr.subs(x, x1)
y2 = expr.subs(x, x2)
avg_slope = (y2-y1)/(x2-x1)

print(f"Expr: {expr}")
print(f"Lets select an interval for x->[{x1},{x2}]")
print(f"Avg. rate of change of expr over [{x1},{x2}]:"
      f"\n\t f(x2)={y2}"
      f"\n\t f(x1)={y1}"
      f"\n\t f(x2)-f(x1)/x2-x1 i.e. avg_slope= {avg_slope}")

# find the slope of the equation
d1_expr = expr.diff(x)
print(f"d1_expr: {d1_expr}")
# solve for the value (x3) that equals the average slope
#     this value should be between closed [x1, x2]
print(f"Solve for x3 as so: \n\t d1_expr = avg_slope")
x3 = sympy.solve(sympy.Eq(d1_expr, avg_slope), x)
print(f"\t We see that x3 values lie in the interval [{x1},{x2}]: \n\t {sympy.N(x3[0])} AND {sympy.N(x3[1])}")

print(f"Double checking to see that x3 values give a slope of {avg_slope}"
      f"\n when substituted in {d1_expr}:\n"
      f"{sympy.N(x3[0])}->{sympy.N(d1_expr.subs(x, x3[0]))}\n"
      f"{sympy.N(x3[1])}->{sympy.N(d1_expr.subs(x, x3[1]))}")

# Plotting graph of the f(x) and f'(x)
sympy.plot(expr,d1_expr, ylim=[-75,75], legend=True, axis=True)