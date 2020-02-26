import DirectcoordinateDescentMethod
import HookeJeevesMethod
import GradientDescentMethod
import NewtonRaphsonMethod


def function(x):
    print("x={}, y={}".format(x[0], x[1]))
    return x[0] ** 2 + 7 * x[1] ** 2 - 3 * x[0] - x[1]

def gradient(x):
    print("x={}, y={}".format(x[0], x[1]))
    return [-2 * x[0] + 3, -14 * x[1] + 1]

def reversedMatrix(x):
    print("x={}, y={}".format(x[0], x[1]))
    return [[-1/2, 0], [0, -1/14]]

results = []
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01), "DirectcoordinateDescentMethod"))
results.append((HookeJeevesMethod.FindMinimum(function, [0, 0], 0.1, 0.01), "HookeJeevesMethod"))
results.append((GradientDescentMethod.FindMinimum(function, gradient, [0, 0], 0.01, 0.01, 0.01), "GradientDescentMethod"))
results.append((NewtonRaphsonMethod.FindMinimum(function, gradient, reversedMatrix, [0, 0], 0.01, 0.01, 0.01), "NewtonRaphsonMethod"))

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