import sympy
from sympy import symbols
from sympy.solvers import solve

############################
# sample problem 1
############################
def solve_eqn(x_val, f_x):
    print("Running my module...limits_sympy_solve_eqn")
    return solve(f_x, x_val)


if __name__ == '__main__':
    # define the variable
    x = symbols('x')
    # define the equation
    eq = x**2 - 4
    print(f"solution = {solve_eqn(x, eq)}")

# x = symbols('x')
# # Equation of interest
# eq = x**2 - 4
# # solve() sets the equation equal to 0
# print("x = ", solve(eq,x))
