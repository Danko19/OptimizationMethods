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

func = lambda x: -(x[0] ** 2) - 7 * x[1] ** 2 + 3 * x[0] + x[1]
result = DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.01, 0.01)
print(result)

result = HookeJeevesMethod.FindMinimum(function, [0, 0], 0.1, 0.01)
print(result)

result = GradientDescentMethod.FindMinimum(function, gradient, [0, 0], 0.01, 0.01, 0.01)
print(result)

result = NewtonRaphsonMethod.FindMinimum(function, gradient, reversedMatrix, [0, 0], 0.01, 0.01, 0.01)
print(result)