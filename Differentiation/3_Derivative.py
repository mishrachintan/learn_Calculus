import sympy

# Find the derivative of the function x**3
x = sympy.symbols('x')
expr = x**3
derivative = sympy.diff(expr,x)
print("==================================================")
print(f"Derivative of {sympy.latex(expr)}:\n {sympy.latex(derivative)}")

# Find the derivative at a point x=6
#   the derivative of x**3 is already calculated in previoys step
x_val = 6
derivative_val = derivative.subs(x,x_val) # substitute x_val at x
print("==================================================")
print(f"The value of derivative of {expr} at x={x_val}:\n {derivative_val}")

###################################################
# CHAIN RULE
#   this is handled in sympy
###################################################
x, y1, y2 = sympy.symbols('x y1 y2')
y1 = (x**2 + 1)**3
y2 = sympy.sqrt(x**2 + 5)
deriv = sympy.diff(y1,x)
deriv_1 = sympy.diff(y2,x)
print("==================================================")
print("Chain Rule: Example 1")
print(f" Derivative of {y1}:\n {deriv}")
print("==================================================")
print("Chain Rule: Example 2")
print(f" Derivative of {y2}:\n {deriv_1}")
print("==================================================")

###################################################
# PRODUCT RULE
#   if it is a product of 2 functions as so:
#      f1*f2
#   then derivative is calculated as so:
#      derivative(f1)*f2 + derivative(f2)*f1
###################################################
x, y = sympy.symbols('x y')
y = x**3 * sympy.exp(2*x)
deriv_of_y = sympy.diff(y, x)
print("Product Rule: f1*f2")
print(" Formula: derivative(f1)*f2 + derivative(f2)*f1")
print(f"  Derivative of {y}:\n {deriv_of_y}")
print("==================================================")

#####################################################
# QUOTIENT RULE
#   if it is a fraction of 2 functions as so:
#      f1/f2
#   then derivative is calculated as so:
#      (f2*derivative(f1) - f1*derivative(f2))/f2**2
#####################################################
x, y = sympy.symbols('x y')
y = x**2 / sympy.exp(x)
deriv_of_y = sympy.diff(y, x)
print("Quotient Rule: f1/f2")
print(" Formula: (f2*derivative(f1) - f1*derivative(f2))/f2**2")
print(f"  Derivative of {y}:\n {deriv_of_y}")
print("==================================================")

#####################################################
x, y1, y2, y3 = sympy.symbols('x y1 y2 y3')
y1 = 3**x
y2 = sympy.log(x)
base = 3
y3 = sympy.log(x, base)

d_y1 = sympy.diff(y1, x)
d_y2 = sympy.diff(y2, x)
d_y3 = sympy.diff(y3, x)
print("Derivatives of some more standard functions")
print(f"  Derivative of {y1}:\n   {d_y1}")
print(f"  Derivative of {y2}:\n   {d_y2}")
print(f"  Derivative of {y3}:\n   {d_y3}")
print("==================================================")

#########################################################
#    Note: If you desire, better to remember the standard
#           differentiation results for trig functions
#########################################################
print("Interesting result with trigonometric functions: tan(x)")
x, y = sympy.symbols('x y')
y = sympy.tan(x)
derv = sympy.diff(y,x)
print(f"  Derivative of {y}:\n   {derv}")
print("Notice how it is 1+tan(x)**2 and not sec(x)**2, "
      "thats how sympy calcuates")
print("==================================================")

#########################################################
# IMPLICIT DIFFERENTIATION:
#    Here both x and y are on the same side
#########################################################
x, y = sympy.symbols('x y')
eq = x**2 + y**2 - 25
impl_diff = sympy.idiff(eq, y, x)
print(" The eqn that is differentiated implicitly is in fact \n"
      "  x**2 + y**2 = 100, which is evaluated as:\n"
      "  f'(x).y + (dy/dx).x = 0 (cause diff of constant is zero)")
print(f"  \n Hence, Implicit Derivative of equation {eq}:\n   {impl_diff}")
print("--------------------------------------------------")

#########################################################
# Find the value of the derivative at (3,4)
#########################################################
x_val = 3
y_val = 4
ans_x = impl_diff.subs(x, x_val) # Only substitites x
print(f"   Impl. derivative after substituting for x={x_val}: {ans_x}")
ans_y = ans_x.subs(y, y_val)
print(f"   Impl. derivative after substituting for y={y_val} in {ans_x}: {ans_y}")
print("==================================================")

# Plot the eq
#sympy.plotting.plot_implicit(eq, x_var=(x, -15, 15),
#                             y_var=(y, -15, 15))

#########################################################
# Solve for y in the above equation for a given x value
#########################################################
x_val = 3

x_part = eq.subs(x, x_val)
print(f"eq={eq}, \nx_val={x_val}, \n\teq.subs(x, x_val)={x_part}")
print(f" Now make {x_part} equal to zero in order to solve for y, hence:")
y_part = sympy.Eq(x_part, 0)
print(f"\t Equation form in sympy: {y_part}")
print(f" Solving the equation, value of y is")
y_val = sympy.solve(y_part)
print(f"\t {y_val}")

#########################################################
# Solve for derivative/s at x=3
#########################################################
print(f" There can be multiple derivatives at x_val={x_val}")
for i in y_val:
      diff = impl_diff.subs([(x, x_val), (y, i)])
      print(f"\tslope at ({x_val},{i}):{diff}")

###########################################################
# Plot graph for an implicit function
#     The below eqn will have 3 y values for some x values
###########################################################
x, y = sympy.symbols('x y')
eqn = x**3 - 6*x*y + y**3
sympy.plot_implicit(eqn)