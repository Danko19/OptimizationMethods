from typing import Callable
import math

# находим минимум функции одной переменной, на вход подаём:
# a, b - границы отрезка унимодальности
# e - точность для окончания итераций
# func - целевая функция одной переменной 
def FindMinimum(a: float, b: float, e: float, func: Callable[[float], float]) -> (float,float):
    print("Called FindMinimum by FibonacciMethod with params a={}, b={}, e={}".format(a, b, e))
    d = b - a
    fibonacci = TakeThreeFibonacciNumbersWhileLessThan(d / e)
    update_fx = True
    update_fy = True
    iterations = 0
    measurements = 0
    k = 0
    while True:
        iterations += 1
        if update_fx:
            x = a + (b - a) * fibonacci[-3 - k] / fibonacci[-1-k]
            fx = func(x)
            update_fx = False
            measurements += 1
        if update_fy:
            y = a + (b - a) * fibonacci[-2 - k] / fibonacci[-1-k]
            fy = func(y)
            update_fy = False
            measurements += 1
        if fx > fy:
            fmin = fy
            xmin = y
            a = x
            x = y
            fx = fy
            update_fy = True
        else:
            fmin = fx
            xmin = x
            b = y
            y = x
            fy = fx
            update_fx = True
        k += 1
        if b - a < e:
            print("Iterations count={}, measurements count={}".format(iterations, measurements))
            return (xmin, fmin)

# ищем первые l чисел Фибоначчи
def TakeThreeFibonacciNumbersWhileLessThan(l: float):
    fubonacci = [1, 1, 2]
    while fubonacci[-1] < l:
        fubonacci.append(fubonacci[-1] + fubonacci[-2])
    return fubonacci