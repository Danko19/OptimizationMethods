from typing import List
from typing import Tuple
from typing import Callable
import math

def FindMinimum(func: Callable[[List[float]], float], gradient: Callable[[List[float]], List[float]], startPoint: List[float], ed: float, ex: float, ef: float, H) -> List[Tuple[List[float], float]]:
    trace = [(startPoint.copy(), func(startPoint))]
    ds = []
    while True:
        (currentPoint, currentValue) = trace[-1]
        if len(ds) == 0:
            d = GetMultiply(gradient(currentPoint), -1)
            ds.append(d)
        else:
            (previousPoint, _) = trace[-2]
            b = (GetLength(gradient(currentPoint)) ** 2) / (GetLength(gradient(previousPoint)) ** 2)
            d = GetSum(GetMultiply(gradient(currentPoint), -1), GetMultiply(ds[-1], b))
            ds.append(d)
        if GetLength(d) <= ed:
            if len(trace) == 1:
                return trace
            (oldPoint, oldValue) = trace[-2]
            if GetDistance(oldPoint, currentPoint) <= ex and abs(oldValue - currentValue) <= ef:
                return trace
        l = GetScalar(d, GetMultiply(gradient(currentPoint), -1)) / GetScalar(GetMatrixMultiply(H, d), d)
        newPoint = GetSum(currentPoint, GetMultiply(d, l))
        newValue = func(newPoint)
        trace.append((newPoint, newValue))


def GetSum(firstVector: List[float], secondVector: List[float]) -> List[float]:    
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    result = firstVector.copy()
    for i in range(len(firstVector)):
        result[i] = firstVector[i] + secondVector[i]
    return result


def GetMultiply(vector: List[float], multiplier: float) -> List[float]:   
    result = vector.copy()
    for i in range(len(vector)):
        result[i] = vector[i] * multiplier
    return result


def GetLength(vector: List[float]) -> float:
    i = 0
    distance = 0
    while i < len(vector):
        distance += vector[i] ** 2
        i += 1
    return math.sqrt(distance)
    

def GetDistance(firstVector: List[float], secondVector: List[float]) -> float:
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    i = 0
    distance = 0
    while i < len(firstVector):
        distance += (firstVector[i] - secondVector[i]) ** 2
        i += 1
    return math.sqrt(distance)

def GetScalar(firstVector: List[float], secondVector: List[float]) -> float:
    result = 0
    for i in range(len(firstVector)):
        result += firstVector[i] * secondVector[i]
    return result

def GetMatrixMultiply(matrix: List[List[float]], vector: List[float]) -> List[float]:   
    result = vector.copy()
    for i in range(len(vector)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j] * vector[j]
        result[i] = sum
    return result