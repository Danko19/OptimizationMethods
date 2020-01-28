from SvennMethod import FindUnimodalSegment
import DichotomyMethod
import DivisionMethod
import GoldenRatioMathod
import FibonacciMethod

func = lambda x: x ** 2 + 1
(a, b) = FindUnimodalSegment(-5, 0.1, func)
print(a)
print(b)

(x, y) = DichotomyMethod.FindMinimum(-5, 1, 0.01, 0.1, func)
print(x, y)

(x, y) = DivisionMethod.FindMinimum(-5, 1, 0.1, func)
print(x, y)

(x, y) = GoldenRatioMathod.FindMinimum(-5, 1, 0.1, func)
print(x, y)

(x, y) = FibonacciMethod.FindMinimum(-5, 1, 0.1, func)
print(x, y)