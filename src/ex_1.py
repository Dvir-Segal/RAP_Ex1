import inspect
import math
import sys

import sympy as sp
from mpmath import *
from sympy import lambdify

x = sp.Symbol('x')

def find_root(f, a:float, b:float) -> float:
    sqrt = b
    for i in range(10):
        sqrt = sqrt - f(sqrt)/diff(f, sqrt)
    return sqrt
"""Return the sqrt of function in range [a, b], by Newton-Rapson method"""


def safe_call(f, **kwargs):
    try:
        if len(kwargs)!=f.__code__.co_argcount:
            sys.exit(1)
        for var in f.__code__.co_varnames:
            if str(var) in f.__annotations__.keys():
                if f.__annotations__[str(var)]!=type(kwargs[str(var)]):
                    sys.exit(1)
        return f(**kwargs)
    except:
        return "raises an exception"
"""Check matching of arguments list size and types for the  method signature"""

def f(x: int, y: float, z):
    return x*z/y

def g(x: str, y: list):
    return {x: y}



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(find_root(lambda x: x**x-2, 1, 3))
    print(find_root(lambda x: math.log2(x) - 11*x + 5, 0, 1))
    print(find_root(lambda x: math.log(x, math.e) - 7 * x + 17, 0, 54))
    print(find_root(lambda x: math.log2(x**3) - 8*x**2 + 29, 0, 2.5))
    print(find_root(lambda x: math.log(.5*x**3, math.e) - 24 * x + 16, 0, 1))


    print(safe_call(f, x=15, y=7.0, z=3))
    print(safe_call(f, x=5, y="divide", z=3))
    print(safe_call(f, x=9, y=5.8, z=5, w=54))
    print(safe_call(g, x="dfgd", y=("rgfd")))
    print(safe_call(g, x=9, y={'a': 4.0}))
    print(safe_call(g, x="9, y={'a': 4.0}"))
    print(safe_call(g, x="abc", y=[1,2,3]))




