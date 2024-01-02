import random, copy

def neighbor(f, x, h):
    x += random.uniform(-h, h)
    return f(x), x

def hillClimbing(f, x, h = 0.001):
    if f(x) <= 0:
        print("請更換初始值, 使多項式結果大於 0")
        return

    failCount = 0

    while (failCount < 10000):
        fnow = f(x)
        fneighbor, newx = neighbor(f, copy.copy(x), h)

        if fneighbor < fnow:
            if fneighbor <= 0:
                break

            x = newx
            print("x=", x, "f(x)=", fneighbor)
            failCount = 0
        else:
            failCount = failCount + 1
    else:
        print("無實數解")

def f(x):
    return x**5 + 1

hillClimbing(f, 0)

#來源 : https://github.com/LeeYi-user/alg112a/blob/master/homework/10/homework.py
#ChatGPT注釋
neighbor 函数：给定一个函数 f、当前位置 x 和步长 h，它会在当前位置的附近随机选择一个新的位置，并返回新位置的函数值和新位置。

hillClimbing 函数：接受一个目标函数 f、初始位置 x 和步长 h。在每次迭代中，它检查当前位置的函数值，并通过调用 neighbor 函数找到附近的一个新位置。如果新位置的函数值更小（更优），则移动到新位置，并打印出当前位置和函数值。如果新位置的函数值小于等于零，算法终止，因为我们要找的是多项式的零点。如果在连续的迭代中未找到更优的解，循环将终止，并输出 "无实数解"。

f 函数：定义了要解的多项式，这里是 x^5 + 1。

调用 hillClimbing(f, 0)：这是运行算法的主要部分。它使用初始位置 0 调用 hillClimbing 函数。

请注意，爬山算法是一种局部搜索算法，它容易陷入局部最小值。在这个实现中，算法在每次迭代中都会随机选择新的位置，以尝试避免陷入局部最小值。
