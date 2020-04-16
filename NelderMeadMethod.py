import math

# находим минимум функции нескольких переменных, на вход подаём:
# func - исходная функция
# X0 - начальная точка
# el - точность для максимальной длины ребра для окончания итераций
# ef - точность для СКО значенией функции для окончания итераций
# alfa - коэффициент растяжения 
# beta - коэффициент сжатия
# beta - коэффициент редуцирования
# l - начальная длина ребра
def FindMinimum(func, X0, el, ef, alfa = 3, beta = 0.5, gamma = 0.5, l = 10):
    n = len(X0)
    r1 = l * (math.sqrt(n + 1) + n - 1) / (n * math.sqrt(2))
    r2 = l * (math.sqrt(n + 1) - 1) / (n * math.sqrt(2))
    X = [X0]
    for col in range(n):
        X.append([])
        for row in range(n):
            if col == row:
                res = X0[row] + r1
            else:
                res = X0[row] + r2
            X[col + 1].append(res)
    F = []
    for x in X:
        F.append(func(x))
    trace = [(X.copy(), F.copy())]
    while True:
        F_sorted = F.copy()
        F_sorted.sort(reverse=True)
        f_h = F_sorted[0]
        f_l = F_sorted[-1]
        f_g = F_sorted[1]
        i_h = F.index(f_h)
        i_l = F.index(f_l)
        i_g = F.index(f_g)
        x_h = X[i_h]
        x_l = X[i_l]
        x_g = X[i_g]
        x_n2 = get_x_n2(X, i_h)
        x_n3 = minus(multiply(x_n2, 2), x_h)
        f_n3 = func(x_n3)
        if f_n3 <= f_l:
            x_n4 = plus(multiply(x_n2, 1 - alfa), multiply(x_n3, alfa))
            f_n4 = func(x_n4)
            if f_n4 <= f_n3:
                X[i_h] = x_n4
                F[i_h] = f_n4
            else:
                X[i_h] = x_n3
                F[i_h] = f_n3
        elif f_g < f_n3 < f_h:
            x_n5 = plus(x_n2, multiply(minus(x_h, x_n2), beta))
            f_n5 = func(x_n5)
            X[i_h] = x_n5
            F[i_h] = f_n5
        elif f_l < f_n3 <= f_g:
            X[i_h] = x_n3
            F[i_h] = f_n3
        elif f_n3 >= f_h:
            for i in range(len(X)):
                if i == i_l:
                    continue
                X[i] = plus(x_l, multiply(minus(X[i], x_l), gamma))
                F[i] = func(X[i])
        else:
            raise Exception("Something went wrong")
        trace.append((X.copy(), F.copy()))
        if getSKO(F) < ef and getMaxLength(X) < el:
            return trace

# находим координаты точки x_n2
def get_x_n2(X, i_h):
    n = len(X) - 1
    x_n2 = [0] * n 
    for i in range(len(X)):
        if i != i_h:
            for j in range(n):
                x_n2[j] += X[i][j]
    for i in range(n):
        x_n2[i] /= n
    return x_n2

# находим разность двух векторов (новый вектор)
def minus(X1, X2):
    res = [0] * len(X1)
    for i in range(len(X1)):
        res[i] = X1[i] - X2[i]
    return res

# находим cумму двух векторов (новый вектор)
def plus(X1, X2):
    res = [0] * len(X1)
    for i in range(len(X1)):
        res[i] = X1[i] + X2[i]
    return res

# находим произведение вектора на число (новый вектор)
def multiply(X1, m):
    res = [0] * len(X1)
    for i in range(len(X1)):
        res[i] = X1[i] * m
    return res

# находим СКО значений функции
def getSKO(F):
    f_avg = getAVG(F)
    D = 0
    for i in range(len(F)):
        D += (F[i] - f_avg) ** 2
    return D / len(F)

# находим среднее значение функции
def getAVG(F):    
    f_avg = 0
    for i in range(len(F)):
        f_avg += F[i]
    return f_avg / len(F)

# находим максимальную длину ребра
def getMaxLength(X):
    maximum = -math.inf
    for i in range(len(X)):
        for j in range(i + 1, len(X)):
            dist = getDistance(X[i], X[j])
            if dist > maximum:
                maximum = dist
    return maximum

# находим расстояние между двумя точками
def getDistance(X1, X2):
    dist = 0
    for i in range(len(X1)):
        dist += (X1[i] - X2[i]) ** 2
    return math.sqrt(dist)