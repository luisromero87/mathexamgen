import os
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.polys.polytools import degree
import random
from .helper import alpha, digits_nozero, get_coefficients, render, shuffle

def poly1(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(get_coefficients(2)))])
    return vals

def poly2(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(get_coefficients(3)))])
    return vals

def poly3(x):
    vals = sum([k*x**i for i,k in enumerate(reversed(get_coefficients(4)))])
    return vals

def polyn(x, order=3):
    vals = sum([k*x**i for i,k in enumerate(reversed(get_coefficients(order)))])
    return vals

_functions = [sympy.sin, sympy.cos, sympy.tan, sympy.ln, sympy.sqrt, sympy.exp,
              lambda a: a, poly1, poly2, poly3]

def make_find_derivative_at_value(var="x", rhs = "4"):
    F = sympy.Function("f")
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    df = sympy.prod([var - random.choice(digits_nozero) for i in range(random.randint(2,3))])
    f = poly3(var)
    df = int(sympy.diff(f, var).evalf(subs={var:int(rhs)}))

    eq = sympy.latex(sympy.Derivative(F(rhs), var)) 
    eq = 'd'.join(eq.split("\\partial"))
    eq = eq + "=" + str(df)
    fx = "f \\left(%s \\right)" % str(var)
    return render(f, fx), render(eq)


def make_horizontal_tangents(var="x"):
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    df = sympy.prod([var - random.choice(digits_nozero) for i in range(random.randint(2,3))])
    f = sympy.integrate(df, var)
    eqn = sympy.Eq(sympy.diff(f, var),0 )
    fx = "f \\left(%s \\right)" % str(var)
    return render(f, fx), render(', '.join([str(var) + "=" + str(i) for i in sympy.solve(eqn)]))

def make_chain_rule_prob(var="x", partial=False):
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    f1 = random.choice(_functions)
    f2 = random.choice(_functions)
    f3 = random.choice(_functions)

    eq = f2(f1(var)) + f3(var)
    
    sol = sympy.latex(sympy.diff(eq, var))
    eq = sympy.latex(sympy.Derivative(eq, var))
    if not partial:
        eq = 'd'.join(eq.split("\\partial"))
    eq = "$$" + eq + "$$"
    sol = "$$" + sol + "$$"
    return eq, sol

def make_quotient_rule_prob(var="x", partial=False):
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    f1 = random.choice(_functions)
    f2 = random.choice(_functions)
    f3 = random.choice(_functions)

    eq = (f1(var) + f2(var)) / f3(var)
    
    sol = sympy.latex(sympy.diff(eq, var))
    eq = sympy.latex(sympy.Derivative(eq, var))
    if not partial:
        eq = 'd'.join(eq.split("\\partial"))
    eq = "$$" + eq + "$$"
    sol = "$$" + sol + "$$"
    return eq, sol


def make_int_poly_prob(var="x", order=3):
    """
    Generates a n-order polynomial to be integrated.

    x : charector for the variable to be solved for. defaults to "x".
                            OR
        a list of possible charectors. A random selection will be made from them.
    n : order of the polynomial or a list of possible orders. Defaults to 3.
        A random selection will be made from them.

    """
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    if isinstance(order, list):
        order = random.choice(order)

    eq = polyn(var,order)
    
    sol = sympy.latex(sympy.integrate(eq, var))
    eq = sympy.latex(sympy.Integral(eq, var))
    eq = 'd'.join(eq.split("\\partial"))
    eq = "$$" + eq + "$$"
    sol = "$$" + sol + " + C $$"
    return eq, sol

def make_int_pow_prob(var="x", order=3):
    """
    Generates a n-order polynomial to be integrated.

    x : charector for the variable to be solved for. defaults to "x".
                            OR
        a list of possible charectors. A random selection will be made from them.
    n : order of the polynomial or a list of possible orders. Defaults to 3.
        A random selection will be made from them.

    """
    if isinstance(var, str):
        var = sympy.Symbol(var, positive=True)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var), positive=True)
    if isinstance(order, list):
        order = random.choice(order)
    eq = 0;
    sol = 0;
    length = random.randint(1,3)
    for i in range(1,length+1):
        a = random.randint(1,10)*random.choice([-1,1])
        b = random.randint(1,10)
        n = random.randint(1,5)
        while (not n%order):
            n = random.randint(1,5)
        if (True):
            sign = random.choice([-1,1])
            eq += sympy.Rational(a,b)*(var**sympy.Rational(n,order))**sign
            sol+= sympy.Rational(a*(n*sign+order),b*order)*(var**sympy.Rational(n*sign+order,order))
        else:
            eq += (sympy.Rational(a,b)*sympy.root(var**n,order))**random.choice([-1,1])
    
    sol = sympy.latex(sol)
    eq = sympy.latex(sympy.Integral(eq, var))
    eq = 'd'.join(eq.split("\\partial"))
    eq = "$$" + eq + "$$"
    sol = "$$" + sol + " + C $$"
    return eq, sol

def make_int_sust_prob(var="x"):
    """
    Generates a n-order polynomial to be integrated.

    x : charector for the variable to be solved for. defaults to "x".
                            OR
        a list of possible charectors. A random selection will be made from them.
    n : order of the polynomial or a list of possible orders. Defaults to 3.
        A random selection will be made from them.

    """
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    func1 = random.choice(_functions)
    func2 = random.choice(_functions)
    g = func2(var)
    f = func1(g)
    dg = sympy.diff(g,var)
    eq = f*dg
    
    sol = sympy.latex(sympy.integrate(eq, var))
    eq = sympy.latex(sympy.Integral(eq, var))
    eq = 'd'.join(eq.split("\\partial"))
    eq = "$$" + eq + "$$"
    sol = "$$" + sol + " + C $$"
    return eq, sol


def make_poly_ratio_limit(var="x", s=[0, 1, 2]):
    """
    Generates a ratio of two polynomials, and evaluates them at infinity.

    x : charector for the variable to be solved for. defaults to "x".
                            OR
        a list of possible charectors. A random selection will be made from them.

    s : selects the kind of solution
        0 : limit at infinity is zero
        1 : limit as infinity is a nonzero finite number
        2 : limit at infinity is either +infinity or -infinity

        default: one of the above is randomly selected
    """
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    if isinstance(s, list):
        s = random.choice(s)
    if s == 2: # infinity
        p1 = random.randint(2, 4)
        p2 = p1-1
    elif s == 1: # ratio of leading coefficients
        p1 = random.randint(2, 4)
        p2 = p1
    elif s == 0: # zero
        p1 = random.randint(2, 4)
        p2 = random.randint(p1, p1 + 2)
    select = [shuffle(digits_nozero)[0]] + shuffle(list(range(10))[:p1-1])
    num = sum([(k+1)*var**i for i, k in enumerate(select)])
    select = [shuffle(digits_nozero)[0]] + shuffle(list(range(10))[:p2-1])
    denom = sum([(k+1)*var**i for i, k in enumerate(select)])
    e = num / denom
    s = sympy.limit(e, var, sympy.oo)

    e = "\lim_{x \\to \infty}" + sympy.latex(e)
    return render(e), render(s)

if __name__ == "__main__":
    print(make_poly_ratio_limit(["x", "y"]))