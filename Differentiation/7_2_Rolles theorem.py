import sympy

st = """===============================================================
Rolle's Theorem:
    Like a variant of the mean value theorem.
    If the function is continous on closed interval [a, b] and
    differentiable in open interval (a,b) such that f(a) == f(b)
    then there exists at east one point c in [a,b] such that
        f'(c) = 0. 
        
        *Note: f(a) == f(b), hence f(b)-f(a)/b-a = 0
===============================================================
"""
print(st)

# Make the expression and differentiate it
x, y = sympy.symbols('x y')
y  = (x-4)**2
dy = sympy.diff(y, x)

# Pick x1 and x2:
#   Note: we here picked x1, x2 such that
#   slope can be calulated as zero
x1 = 10
y1 = y.subs(x, x1)
x2 = -2
y2 = y.subs(x, x2)

# find the slope, this should be zero
slope = (y2-y1)/(x2-x1)

# Do dy=slope and solve for x
x3 = sympy.solve(sympy.Eq(dy, slope), x)
# check if f'(x3) is zero i.e same as slope
assert dy.subs(x, x3[0]) == slope

# solve for respective y value and plot in in a graph
y3 = y.subs(x, x3[0])
label = str((x3[0], y3))
sympy.plot(y,dy, ylim=[-20,20], legend=True, axis=True, markers=[{'args': [x3, 0, 'go'], "label":label}])