from typing import Callable
import math

# находим минимум функции одной переменной, на вход подаём:
# a, b - границы отрезка унимодальности
# e - точность для окончания итераций
# func - целевая функция одной переменной 
def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float,float):
    print("Called FindMinimum by GoldenRatioMathod with params a={}, b={}, e={}".format(a, b, e))
    t = (math.sqrt(5) - 1) / 2
    d = b -a
    dif = t * d
    y = a + dif
    x = b - dif
    update_fx = True
    update_fy = True
    iterations = 0
    measurements = 0
    while True:
        iterations += 1
        if update_fx:
            fx = func(x)
            update_fx = False
            measurements += 1
        if update_fy:
            fy = func(y)
            update_fy = False
            measurements += 1
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
            print("Iterations count={}, measurements count={}".format(iterations, measurements))
            return (xmin, fmin)