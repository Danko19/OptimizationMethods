from typing import Callable
import math

def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float,float):
    t = (math.sqrt(5) - 1) / 2
    d = b -a
    dif = t * d
    y = a + dif
    x = b - dif
    update_fx = True
    update_fy = True
    while True:
        if update_fx:
            fx = func(x)
            update_fx = False
        if update_fy:
            fy = func(y)
            update_fy = False
        if fx > fy:
            fmin = fy
            xmin = y
            a = x
            x = y
            fx = fy
            y = a + b - x
            update_fy = True
        else:
            fmin = fx
            xmin = x
            b = y
            y = x
            fy = fx
            x = a + b - y
            update_fx = True
        if b - a < e:
            return (xmin, fmin)