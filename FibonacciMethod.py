from typing import Callable
from queue import Queue
import math

def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float,float):
    d = b - a
    fibonacci = TakeThreeFibonacciNumbersWhileLessThan(d / e)
    x = a + fibonacci[0] / fibonacci[2] * d
    y = a + fibonacci[1] / fibonacci[2] * d
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

def TakeThreeFibonacciNumbersWhileLessThan(l: float):
    fubonacci = [1, 1, 2]
    while fubonacci[2] < l:
        fubonacci[0] = fubonacci[1]
        fubonacci[1] = fubonacci[2]
        fubonacci[2] = fubonacci[0] + fubonacci[1]
    return fubonacci