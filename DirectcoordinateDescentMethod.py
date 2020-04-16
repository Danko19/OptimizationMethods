from typing import List
from typing import Tuple
from typing import Callable
import math

# находим минимум функции нескольких переменных, на вход подаём:
# func - исходная функция
# startPoint - начальная точка
# e1, e2 - точность значений функции и точки для окончания итераций
# findMinFunc - функция одномерной оптимизации 
def FindMinimum(func: Callable[[List[float]], float], startPoint: List[float], e1: float, e2: float, findMinFunc) -> List[Tuple[List[float], float]]:
    steps = len(startPoint)
    position = startPoint.copy()
    trace = [(position.copy(), func(position))]
    while True:
        step = 0
        while step < steps:
            singleVarFunc = GetSignleVariableFunc(func, position, step)
            (x, _) = findMinFunc(singleVarFunc, position[step])
            position[step] = x
            step += 1
        value = func(position)
        trace.append((position.copy(), value))
        (previousPosition, previousValue) = trace[-2]
        if GetDistance(position, previousPosition) <= e1 and abs(value - previousValue) <= e2:
            return trace

# фиксируем начальную точку и направление и создаём функцию одной переменной
def GetSignleVariableFunc(func: Callable[[List[float]], float], values: List[float], step: int) -> Callable[[float], float]:
    copy = values.copy()
    def inner(x: float) -> float:
        copy[step] = x
        return func(copy)
    return inner

# ищем расстояние между точками
def GetDistance(firstVector: List[float], secondVector: List[float]) -> float:
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    i = 0
    distance = 0
    while i < len(firstVector):
        distance += (firstVector[i] - secondVector[i]) ** 2
        i += 1
    return math.sqrt(distance)