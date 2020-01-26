from typing import Callable

def FindMinimum(a: float, b: float, d: float, e: float, func: Callable[[float], float]) -> float:
    while True:
        c = (a + b) / 2
        x1 = c - d
        x2 = c + d
        if func(x1) > func(x2):
            a = x1
        else: 
            b = x2
        if abs(b - a) <= e:
            return (a + b) /2