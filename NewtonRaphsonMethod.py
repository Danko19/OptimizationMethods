from typing import List
from typing import Tuple
from typing import Callable
import GoldenRatioMathod
import SvennMethod
import math

def FindMinimum(func: Callable[[List[float]], float], gradient: Callable[[List[float]], List[float]], reverseMatrix: Callable[[List[float]], List[List[float]]], startPoint: List[float], ed: float, ex: float, ef: float) -> List[Tuple[List[float], float]]:
    trace = [(startPoint.copy(), func(startPoint))]
    while True:
        (previousPoint, previousValue) = trace[-1]
        grad = gradient(previousPoint)
        if GetLength(grad) <= ed:
            if len(trace) == 1:
                return trace
            (oldPoint, oldValue) = trace[-2]
            if GetDistance(oldPoint, previousPoint) <= ex and abs(oldValue - previousValue) <= ef:
                return trace
        matrix = reverseMatrix(previousPoint)
        direction = GetMatrixMultiply(matrix, grad)
        singleVarFunc = GetSignleVariableFunc(func, previousPoint, direction)
        (a, b) = SvennMethod.FindUnimodalSegment(0, 0.01, singleVarFunc)
        (l, newValue) = GoldenRatioMathod.FindMinimum(a, b, ed / 10, singleVarFunc)
        newPoint = GetSum(previousPoint, GetMultiply(direction, l))
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


def GetMatrixMultiply(matrix: List[List[float]], vector: List[float]) -> List[float]:   
    result = vector.copy()
    for i in range(len(vector)):
        sum = 0
        for j in range(len(matrix[0])):
            sum += matrix[i][j] * vector[j]
        result[i] = sum
    return result


def GetSignleVariableFunc(func: Callable[[List[float]], float], previousPoint: List[float], direction: List[float]) -> Callable[[float], float]:
    def inner(l: float) -> float:
        newPoint = GetSum(previousPoint, GetMultiply(direction, l))
        return func(newPoint)
    return inner


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