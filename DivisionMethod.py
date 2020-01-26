from typing import Callable

def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float, float):
    x = (a + b) / 2
    fx = func(x)
    while True:
        l = abs(b - a)
        if l <= e:
            return (x, fx)
        y = a + l / 4
        z = b - l / 4
        fy = func(y)
        fz = func(z)
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