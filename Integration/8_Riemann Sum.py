# Area under curve calculated by dividing the region under
# the curve into smaller rectangular strips. Area of each strip
# is then calculated and summation gives an approx area under
# the curve.

# NOTE: The thinner the strip, the more accurate is the area

import sympy

x, y = sympy.symbols('x y')
y = x**2

# we want to calulate ares in range x=[1,3]
dx = 0.1
x1 = 0
x2 = 3
# Calculate total number of strips
total_rect = int((x2-x1)/dx)

# Calculate the area under teh ccurve by iterating
#   over each strip
x_left = x1
sum_area = 0
for i in range(total_rect):
    x_left = x1 + dx*i
    y_left = y.subs(x, x_left)
    sum_area += dx*y_left

print(f"Area under curve: {sum_area}")