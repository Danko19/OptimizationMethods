from typing import List
from typing import Tuple
from typing import Callable
import math

# находим минимум функции нескольких переменных, на вход подаём:
# func - исходная функция
# startPoint - начальная точка
# delta - длина шага при выборе направления
# e - точность для окончания итераций
# findMinFunc - функция одномерной оптимизации 
# m - коэффициент уменьшения шага при выборе направления
def FindMinimum(func: Callable[[List[float]], float], startPoint: List[float], delta: float, e: float, findMinFunc, m: float = 0.5) -> List[Tuple[List[float], float]]:
    steps = len(startPoint)
    trace = [(startPoint.copy(), func(startPoint))]
    while True:
        (previousPoint, previousValue) = trace[-1]
        newPoint = previousPoint.copy()
        for step in range(steps):
            previousValue = func(newPoint)
            newPoint[step] += delta
            if func(newPoint) < previousValue:
                continue
            newPoint[step] -= delta * 2
            if func(newPoint) < previousValue:
                continue
            newPoint[step] += delta
        direction = GetDifference(newPoint, previousPoint)
        if all(abs(number) < e / 10 for number in direction):
            if delta <= e:
                return trace
            delta *= m
            continue
        singleVarFunc = GetSignleVariableFunc(func, previousPoint, direction)
        (l, newValue) = findMinFunc(singleVarFunc, 0)
        newPoint = GetSum(previousPoint, GetMultiply(direction, l))
        trace.append((newPoint, newValue))

# находим разность двух векторов (новый вектор)
def GetDifference(firstVector: List[float], secondVector: List[float]) -> List[float]:    
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    result = firstVector.copy()
    for i in range(len(firstVector)):
        result[i] = firstVector[i] - secondVector[i]
    return result

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