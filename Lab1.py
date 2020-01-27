from SvennMethod import FindUnimodalSegment
import DichotomyMethod
import DivisionMethod
import GoldenRatioMathod

func = lambda x: x ** 2 + 1
(a, b) = FindUnimodalSegment(-5, 0.1, func)
print(a)
print(b)

solve = DichotomyMethod.FindMinimum(-5, 1, 0.01, 0.1, func)
print(solve)

(x, y) = DivisionMethod.FindMinimum(-5, 1, 0.1, func)
print(x, y)

(x, y) = GoldenRatioMathod.FindMinimum(-5, 1, 0.1, func)
print(x, y)