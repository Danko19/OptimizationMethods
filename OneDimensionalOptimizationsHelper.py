from typing import Callable
import SvennMethod
import GoldenRatioMathod
import PowellsMethod
import FibonacciMethod

def GetGoldenRatioMethodFunc(e: float):
    def inner(singleVarFunc, approximation):
        (a, b) = SvennMethod.FindUnimodalSegment(approximation, 0.01, singleVarFunc)
        return GoldenRatioMathod.FindMinimum(a, b, e / 10, singleVarFunc)
    return inner

def GetPowellsMethodFunc(e: float, d: float):
    def inner(singleVarFunc, approximation):
        return PowellsMethod.FindMinimum(approximation, e, e, d, singleVarFunc)
    return inner

def GetFibonacciMethodFunc(e: float):
    def inner(singleVarFunc, approximation):
        (a, b) = SvennMethod.FindUnimodalSegment(approximation, 0.01, singleVarFunc)
        return FibonacciMethod.FindMinimum(a, b, e / 10, singleVarFunc)
    return inner