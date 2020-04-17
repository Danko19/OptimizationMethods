from typing import List
from typing import Tuple
from typing import Callable
import math

# находим минимум функции нескольких переменных, на вход подаём:
# func - исходная функция
# gradient - функция градиента исходной функции 
# startPoint - начальная точка
# ed, ex, ef - точность значений градиента, точки и фнукции для окончания итераций
# или findMinFunc - функция одномерной оптимизации для поиска длины шага 
# или H - матрица Гессе, для расчётной формулы для поиска шага
def FindMinimum(func: Callable[[List[float]], float], gradient: Callable[[List[float]], List[float]], startPoint: List[float], ed: float, ex: float, ef: float, findMinFunc = None, H = None) -> List[Tuple[List[float], float]]:
    if findMinFunc is None and H is None:
        raise Exception("One of parameters 'findMinFunc' or 'H' should be defined")
    trace = [(startPoint.copy(), func(startPoint))]
    while True:
        (previousPoint, previousValue) = trace[-1]
        direction = gradient(previousPoint)
        if GetLength(direction) <= ed:
            if len(trace) == 1:
                return trace
            (oldPoint, oldValue) = trace[-2]
            if GetDistance(oldPoint, previousPoint) <= ex and abs(oldValue - previousValue) <= ef:
                return trace
        singleVarFunc = GetSignleVariableFunc(func, previousPoint, direction)
        if findMinFunc is not None:
            (l, _) = findMinFunc(singleVarFunc, 0)
        else:
            l = - (GetScalar(direction, direction) / GetScalar(GetMatrixMultiply(H, direction), direction))
        newPoint = GetSum(previousPoint, GetMultiply(direction, l))
        newValue = func(newPoint)
        trace.append((newPoint, newValue))

# находим сумму двух векторов (новый вектор)
def GetSum(firstVector: List[float], secondVector: List[float]) -> List[float]:    
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    result = firstVector.copy()
    for i in range(len(firstVector)):
        result[i] = firstVector[i] + secondVector[i]
    return result

# находим произведение вектора на число (новый вектор)
def GetMultiply(vector: List[float], multiplier: float) -> List[float]:   
    result = vector.copy()
    for i in range(len(vector)):
        result[i] = vector[i] * multiplier
    return result

# фиксируем начальную точку и направление и создаём функцию одной переменной
def GetSignleVariableFunc(func: Callable[[List[float]], float], previousPoint: List[float], direction: List[float]) -> Callable[[float], float]:
    def inner(l: float) -> float:
        newPoint = GetSum(previousPoint, GetMultiply(direction, l))
        return func(newPoint)
    return inner

# находим длину вектора (число)
def GetLength(vector: List[float]) -> float:
    i = 0
    distance = 0
    while i < len(vector):
        distance += vector[i] ** 2
        i += 1
    return math.sqrt(distance)

# находим расстояние между точками
def GetDistance(firstVector: List[float], secondVector: List[float]) -> float:
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    i = 0
    distance = 0
    while i < len(firstVector):
        distance += (firstVector[i] - secondVector[i]) ** 2
        i += 1
    return math.sqrt(distance)

# находим скалярное произведение векторов
def GetScalar(firstVector: List[float], secondVector: List[float]) -> float:
    result = 0
    for i in range(len(firstVector)):
        result += firstVector[i] * secondVector[i]
    return result

# находим произведение матрицы на вектор
def GetMatrixMultiply(matrix: List[List[float]], vector: List[float]) -> List[float]:   
    result = vector.copy()
    for i in range(len(vector)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j] * vector[j]
        result[i] = sum
    return result