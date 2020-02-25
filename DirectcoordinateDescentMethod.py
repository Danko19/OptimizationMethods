from typing import List
from typing import Tuple
from typing import Callable
import GoldenRatioMathod
import SvennMethod
import math

def FindMinimum(func: Callable[[List[float]], float], startPoint: List[float], e1: float, e2: float) -> List[Tuple[List[float], float]]:
    steps = len(startPoint)
    position = startPoint.copy()
    trace = [(position.copy(), func(position))]
    while True:
        step = 0
        while step < steps:
            singleVarFunc = GetSignleVariableFunc(func, position, step)
            (a, b) = SvennMethod.FindUnimodalSegment(position[step], 0.01, singleVarFunc)
            (x, _) = GoldenRatioMathod.FindMinimum(a, b, e1 / 10, singleVarFunc)
            position[step] = x
            step += 1
        value = func(position)
        trace.append((position.copy(), value))
        (previousPosition, previousValue) = trace[-2]
        if GetDistance(position, previousPosition) <= e1 and abs(value - previousValue) <= e2:
            return trace


def GetSignleVariableFunc(func: Callable[[List[float]], float], values: List[float], step: int) -> Callable[[float], float]:
    copy = values.copy()
    def inner(x: float) -> float:
        copy[step] = x
        return func(copy)
    return inner

def GetDistance(firstVector: List[float], secondVector: List[float]) -> float:
    if len(firstVector) != len(secondVector):
        raise Exception("Vectors have different number of elements. First={}, second={}".format(len(firstVector), len(secondVector)))
    i = 0
    distance = 0
    while i < len(firstVector):
        distance += (firstVector[i] - secondVector[i]) ** 2
        i += 1
    return math.sqrt(distance)