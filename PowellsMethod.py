# находим минимум функции одной переменной, на вход подаём:
# x0 - начальная точка
# e1, e2 - точность значений функции и точки для окончания итераций
# delta - длина шага
# func - целевая функция одной переменной
def FindMinimum(x0, e1, e2, delta, func):
    x1 = x0
    x2 = x1 + delta
    f1 = func(x1)
    f2 = func(x2)
    if f1 > f2:
        x3 = x2 + delta
    else:
        x3 = x1 - delta
    while True:
        f3 = func(x3)
        fs = [f1, f2, f3]
        f_min = min(fs)
        x_min = [x1, x2, x3][fs.index(f_min)]
        x_avg = 0.5 * (f1 * (x2 ** 2 - x3 ** 2) + f2 * (x3 ** 2 - x1 ** 2) + f3 * (x1 ** 2 - x2 ** 2)) / (f1 * (x2 - x3) + f2 * (x3 - x1) + f3 * (x1 - x2))
        f_avg = func(x_avg)
        if abs(f_min - f_avg) <= e1 and abs(x_min - x_avg) <= e2:
            return (x_min, f_min)
        if x1 <= x2 <= x3 and x_avg >= x2 and x_avg <= x3:
            x1 = x2
            f1 = f2
            x2 = x_avg
            f2 = f_avg
        elif x3 <= x1 <= x2 and x_avg >= x3 and x_avg <= x2:
            x1 = x_avg
            f1 = f_avg
        else:
            x1 = x_avg
            x2 = x1 + delta
            f1 = func(x1)
            f2 = func(x2)
            if f1 > f2:
                x3 = x2 + delta
            else:
                x3 = x1 - delta    