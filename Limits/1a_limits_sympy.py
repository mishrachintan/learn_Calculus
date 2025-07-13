#import sympy
import myownsolve
from sympy import limit, symbols, oo
from sympy.solvers import solve
from sympy.plotting import plot

if __name__ == '__main__':
    x = symbols('x')
    eq_nr = 3*x**2    # numerator eqn
    eq_dr = x**2 - 4  # denominator eqn
    expr = eq_nr/eq_dr # final expression

    # find the roots of the denominator
    #   Note: below part is in fact "solve(f_x, x_val)" i was brushing
    #   up on how to import a module by using myownsolve, so
    #   if desired replace "myownsolve.solve_eqn" by "solve"
    roots = myownsolve.solve_eqn(x, eq_dr)
    print(roots)

    # calculate limit value at the roots for the entire expression
    for r in roots:
        print("---------------------------------------------")
        print(f"When x->{r}: expr gives {limit(expr, x, r)}")
        print(f"From Left: {limit(expr, x, r, dir='-')}")
        print(f"From Right: {limit(expr, x, r, dir='+')}")
        print(f"Without specifying direction: {limit(expr, x, r)}")
        print("---------------------------------------------")

    # calulate limit value at infinity
    print(f"When x->oo: expr gives {limit(expr, x, oo)}")
    print(f"When x->oo-: expr gives {limit(expr, x, -oo)}")

    # plot the graph with sympy
    plot(expr)