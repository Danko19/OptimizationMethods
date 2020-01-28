from typing import Callable

def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float, float):
    print("Called FindMinimum by DivisionMethod with params a={}, b={}, e={}".format(a, b, e))
    x = (a + b) / 2
    fx = func(x)
    iterations = 0
    measurements = 1
    while True:
        l = abs(b - a)
        if l <= e:
            print("Iterations count={}, measurements count={}".format(iterations, measurements))
            return (x, fx)
        y = a + l / 4
        z = b - l / 4
        fy = func(y)
        fz = func(z)
        iterations += 1
        measurements += 2
        if fy < fx:
            b = x
            x = y
            fx = fy
        elif fz < fx:
            a = x
            x = z
            fx = fz
        else:
            a = y
            b = z