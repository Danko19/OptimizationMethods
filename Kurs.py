import DirectcoordinateDescentMethod
import OneDimensionalOptimizationsHelper
import HookeJeevesMethod
import NelderMeadMethod
import GradientDescentMethod
import FletcherReevesMethod


def function(X):
    x = X[0]
    y = X[1]
    return ((x - 3) ** 2) / 2  + ((y - 2) ** 2) / 4

def gradient(X):
    x = X[0]
    y = X[1]
    return [x - 3, y / 2 - 1]

results = []
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetGoldenRatioMethodFunc(0.01)), "DirectcoordinateDescentWithGoldenRationMethod"))
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetPowellsMethodFunc(0.01, 0.01)), "DirectcoordinateDescentPowellsMethod"))
NelderMeadMethod.FindMinimum(function, [0, 0], 0.1, 0.1)
results.append((HookeJeevesMethod.FindMinimum(function, [0, 0], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetFibonacciMethodFunc(0.01)), "HookeJeevesWithFibonacciMethod"))
results.append((GradientDescentMethod.FindMinimum(function, gradient, [0, 0], 0.01, 0.01, 0.01, OneDimensionalOptimizationsHelper.GetGoldenRatioMethodFunc(0.01)), "GradientDescentWithGoldenRationMethod"))
results.append((FletcherReevesMethod.FindMinimum(function, gradient, [0, 0], 0.01, 0.01, 0.01, [[1, 0], [0, 0.4]]), "FletcherReevesMethod"))

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