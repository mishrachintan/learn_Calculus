import sympy

print("=============================================================================")
print("EXAMPLE-1: Ladder falling from an edge:")
print("=============================================================================")
# Create the expression
x, y, t = sympy.symbols('x y t')
expr = x**2 + y**2 - 100

# Note: This is the same as sympy.diff(expr, x)
dx = expr.diff(x)
dy = expr.diff(y)
dxdt = sympy.Derivative(x,t)
dydt = sympy.Derivative(y,t)

d1_expr = dx*dxdt + dy*dydt
print(f"\tExpr: {expr}")
print(f"\t      d1_expr: {d1_expr}")
print(f"\t    Given dxdt=1, y=2, find dydt ")

# directly use sympy.solve, makes the expr = 0 eqn = sympy.Eq(expr, 0)
x_val = sympy.solve(expr.subs(y, 2))[1]# take the positive root
dx_val = dx.subs(x, x_val)
dy_val = dy.subs(y, 2)
print(f"\t     Step 1. Find x value at y=2, which is: {x_val}")
print(f"\t     Step 2. Calculate dx [dx.subs(x, x_val)]: {dx_val}"
      f"\n\t             Calculate dy [dy.subs(y, 2)]    : {dy_val}"
      f"\n\t             Given dxdt                      : 1 m/s")
#dydx = sympy.solve(d1_expr.subs([(dx, dx_val), (dy, dy_val), (dxdt, 1)]))
#print(f"\t     Step 3. Substitute in d1_expr and calculate dydx: {dydx}")
d1_expr_new = d1_expr.subs([(dx, dx_val), (dy, dy_val), (dxdt, 1)])
d1_expr_eq = sympy.Eq(d1_expr_new, 0)
dydt_val = sympy.solve(d1_expr_eq, dydt)
print(f"\t     Step 3. Finally solve for dydt(rate of ladder sliding down): {dydt_val[0]} m/s")

print("\n=============================================================================")
print("EXAMPLE-2: Volume of a balloon (Assume balloon to be sphere for simplicity)")
print("=============================================================================")

v, r, t = sympy.symbols('v r t')

expr = (4/3)*sympy.pi*r**3

dr = expr.diff(r)
drdt = sympy.Derivative(r, t)
dvdt = dr*drdt

print(f"Expr: {expr}")
print(f"\t drdt:{drdt} "
      f"\n\t dr:{dr} "
      f"\n\t dvdt:{dvdt}")

print(f"\n\t calculate drdt: Given that dvdt=9, r=2")
d_eval = dr.subs(r, 2)
print(f"\t  Step 1.Substitute r=2 in dr({dr})->{d_eval}")
d_expr = d_eval*drdt
drdt_eval = sympy.solve(sympy.Eq(d_expr, 9), drdt)
print(f"\t  Step 2.Equate\n\t    {d_expr}=9 and solve for drdt [{drdt}]->{drdt_eval[0]}")