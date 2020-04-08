import DirectcoordinateDescentMethod
import OneDimensionalOptimizationsHelper
import HookeJeevesMethod


def function(X):
    x = X[0]
    y = X[1]
    return ((x - 3) ** 2) / 2  + ((y - 2) ** 2) / 4

results = []
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetGoldenRatioMethodFunc(0.01)), "DirectcoordinateDescentWithGoldenrationMethod"))
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetPowellsMethodFunc(0.01, 0.01)), "DirectcoordinateDescentPowellsMethod"))

results.append((HookeJeevesMethod.FindMinimum(function, [0, 0], 0.1, 0.01, OneDimensionalOptimizationsHelper.GetFibonacciMethodFunc(0.01)), "HookeJeevesWithFibonacciMethod"))

print()
for (result, methodName) in results:
    print()
    print("{} results:".format(methodName))
    stepNumber = 0
    for step in result:
        print("Step {}:".format(stepNumber))
        stepNumber += 1
        dimNumber = 1
        for dim in step[0]:
            print("  x{}={}".format(dimNumber, dim))
            dimNumber += 1
        print("  f(x)={}".format(step[1]))