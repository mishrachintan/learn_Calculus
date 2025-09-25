import sympy as sp

x, y = sp.symbols('x y')
expr = (1/sp.sqrt(2*sp.pi))*sp.exp(-(x**2)/2)

#Plot the curve
#sp.plot(expr, xlim=[-4,4])

# Area under curve give probability
full_area = sp.integrate(expr, (x, -sp.oo, sp.oo))
prob = sp.integrate(expr, (x, -1, 1))
print(f"Full area: sp.integrate(expr, (x, -sp.oo, sp.oo)) --> {full_area}")
print(f"Area(also called Probability): sp.integrate(expr, (x, -1, 1)) --> {sp.N(prob)}")

# Integral is the Error function
err_func = sp.integrate(expr)
sp.plot(expr, err_func, (x, -5, 5))

# Critical value where 95% of the values lie
err_low = err_func.subs(x, -sp.oo)
step1 = sp.Eq(err_func-err_low, 0.95)
step2 = sp.solve(step1, x)[0]
print(f"x-value(also z_value here): sp.Eq(err_func-err_low, 0.95)-->{step2}")

print(f"If you add mean(m) and std_dev(f), then plot as so in interval of 4 std deviations"
      f"to the left and right of mean: \n\t "
      f"sp.plot(expr, err_func, (x, m-4*s, m+4*s))")