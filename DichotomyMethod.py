from typing import Callable

def FindMinimum(a: float, b: float, d: float, e: float, func: Callable[[float], float]) -> (float, float):
    print("Called FindMinimum by DichotomyMethod with params a={}, b={}, d={}, e={}".format(a, b, d, e))
    iterations = 0
    measurements = 0
    while True:
        c = (a + b) / 2
        x1 = c - d
        x2 = c + d
        fx1 = func(x1)
        fx2 = func(x2)
        iterations += 1
        measurements += 2
        if fx1 > fx2:
            a = x1
            fxmin = fx1
            xmin = x1
        else: 
            b = x2
            fxmin = fx2
            xmin = x2
        if abs(b - a) <= e:
            print("Iterations count={}, measurements count={}".format(iterations, measurements))
            return (xmin, fxmin)