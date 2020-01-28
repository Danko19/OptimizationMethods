from SvennMethod import FindUnimodalSegment
import DichotomyMethod
import DivisionMethod
import GoldenRatioMathod
import FibonacciMethod

func = lambda x: x ** 2 + 1
(a, b) = FindUnimodalSegment(-5, 0.1, func)
print("a={}, b={}".format(a, b))
print()

for e in [0.1, 0.01]:        
    (x, y) = DichotomyMethod.FindMinimum(a, b, 0.001, e, func)
    print("x={}, y={}".format(x, y))
    print()
    
    (x, y) = DivisionMethod.FindMinimum(a, b, e, func)
    print("x={}, y={}".format(x, y))
    print()
    
    (x, y) = GoldenRatioMathod.FindMinimum(a, b, e, func)
    print("x={}, y={}".format(x, y))
    print()
    
    (x, y) = FibonacciMethod.FindMinimum(a, b, e, func)
    print("x={}, y={}".format(x, y))
    print()