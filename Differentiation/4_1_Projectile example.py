# Another example with projectile motion equation
#   this is done with distance as a function of time
import sympy

t = sympy.symbols('t')
v = 16.5
h = 3.9

s = -4.9*t**2 + v*t + h

vel = sympy.diff(s)
acc = sympy.diff(vel)

print("=======================================================")
print(f"distance eqn: {s}")
print(f"1st_diff(vel): {vel}")
print(f"2nd_diff(acc): {acc}")
print("=======================================================")

print("Solving for max_height(local maxima where slope is 0):")
# Note: Below directly solves for eqn=0,
#   no need to do use "sympy.Eq(eqn, 0)"
r1 = sympy.solve(vel) # Note: directly solves for eqn=0,
print(f"\t 't' value at highest point = {round(r1[0],2)}")
print(f"\t distance value at {round(r1[0],2)}: {round(s.subs(t, r1[0]),2)}")


