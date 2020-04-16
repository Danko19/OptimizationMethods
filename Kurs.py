import DirectcoordinateDescentMethod
import OneDimensionalOptimizationsHelper
import HookeJeevesMethod
import NelderMeadMethod
import GradientDescentMethod
import FletcherReevesMethod
import matplotlib.pyplot as plt
import numpy as np

save = True
show = False

def function(X):
    x = X[0]
    y = X[1]
    return ((x - 3) ** 2) / 2  + ((y - 2) ** 2) / 4

def gradient(X):
    x = X[0]
    y = X[1]
    return [x - 3, y / 2 - 1]

# получение результатов оптимизации функции разными методами
results = []
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [-2, 8], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetGoldenRatioMethodFunc(0.01)), "Метод прямого покоординатного спуска (золотое сечение)"))
results.append((DirectcoordinateDescentMethod.FindMinimum(function, [-2, 8], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetPowellsMethodFunc(0.01, 0.01)), "Метод прямого покоординатного спуска (метод Пауэлла)"))
results.append((NelderMeadMethod.FindMinimum(function, [-2, 8], 0.1, 0.1), "Метод Нелдера-Мида"))
results.append((HookeJeevesMethod.FindMinimum(function, [-2, 8], 0.01, 0.01, OneDimensionalOptimizationsHelper.GetFibonacciMethodFunc(0.01)), "Метод Хука-Дживса (метод Фибоначчи)"))
results.append((GradientDescentMethod.FindMinimum(function, gradient, [-2, 8], 0.01, 0.01, 0.01, OneDimensionalOptimizationsHelper.GetGoldenRatioMethodFunc(0.01)), "Метод наискорейшего градиентного спуска"))
results.append((FletcherReevesMethod.FindMinimum(function, gradient, [-2, 8], 0.01, 0.01, 0.01, [[1, 0], [0, 0.5]]), "Метод Флетчера-Ривса"))

print()
# вывод пошагового результата каждого метода на консоль
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

# подготовка графика
def prepareGraph(methodName):
    # координатная сетка
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    major_ticks = np.arange(x_min, x_max + 1, 5)
    minor_ticks = np.arange(x_min, x_max + 1, 1)
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)
    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)

    # линии уровня
    delta = 0.025
    x = np.arange(x_min, x_max, delta)
    y = np.arange(y_min, y_max, delta)
    X, Y = np.meshgrid(x, y)
    Z = ((X - 3) ** 2) / 2  + ((Y - 2) ** 2) / 4
    CS = ax.contour(X,Y,Z, [1, 5, 10, 20, 40, 60], colors='#c8c8c8')
    plt.clabel(CS, inline=1, fontsize=10, fmt='%d')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.title(methodName)

# создание графиков для каждого метода
for (result, methodName) in results:
    x_min = -10; x_max = 10; y_min = -10; y_max = 10    
    prepareGraph(methodName)
    if methodName == "Метод Нелдера-Мида":
        i = 0
        for step in result:
            x = [step[0][0][0], step[0][1][0], step[0][2][0], step[0][0][0]]
            y = [step[0][0][1], step[0][1][1], step[0][2][1], step[0][0][1]]
            plt.plot(x,y, '-o', color='#302ab5')
            if save:
                plt.savefig("D:\\screens\\" + methodName + "_" + str(i) + ".png")
            if show:
                plt.show()
            prepareGraph(methodName)
            i += 1
    else:
        x = []
        y = []
        for step in result:
            x.append(step[0][0])
            y.append(step[0][1])
        plt.plot(x,y, '-o', color='#302ab5')
        if save:
            plt.savefig("D:\\screens\\" + methodName + ".png")
        if show:
            plt.show()