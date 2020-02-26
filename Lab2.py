import DirectcoordinateDescentMethod


def function(x):
    print("x={}, y={}".format(x[0], x[1]))
    return x[0] ** 2 + 7 * x[1] ** 2 - 3 * x[0] - x[1]

func = lambda x: -(x[0] ** 2) - 7 * x[1] ** 2 + 3 * x[0] + x[1]
result = DirectcoordinateDescentMethod.FindMinimum(function, [0, 0], 0.1, 0.1)
print(result)