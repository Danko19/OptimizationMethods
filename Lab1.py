from SvennMethod import FindUnimodalSegment
import DichotomyMethod

func = lambda x: x ** 2 + 1
(a, b) = FindUnimodalSegment(-5, 0.1, func)
print(a)
print(b)

solve = DichotomyMethod.FindMinimum(-5, 1, 0.01, 0.1, func)
print(solve)