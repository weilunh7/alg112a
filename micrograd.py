from engine import Value

a = Value(2)
b = Value(1)
c = Value(3)

while True:
    f = a**2 + b**2 + c**2

    print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)
    f.backward()

    if a.grad < 0.001:
        break

    a -= a.grad * 0.01
    b -= b.grad * 0.01
    c -= c.grad * 0.01

#程式來源 : https://github.com/LeeYi-user/alg112a/blob/master/homework/07/homework.py
#相關資訊 : ChatGPT
"""

这段代码使用了 engine 模块中的 Value 类，

它实现了一个简单的梯度下降法来最小化目标函数 f = a**2 + b**2 + c**2。梯度下降法的目标是通过不断调整变量 a、b 和 c 的值，

使得目标函数 f 的值逐渐趋近最小值。

让我解释一下代码的每个部分：

from engine import Value

# 初始化变量 a、b、c
a = Value(2)
b = Value(1)
c = Value(3)

# 梯度下降迭代
while True:
    # 计算目标函数值
    f = a**2 + b**2 + c**2

    # 打印当前变量值和目标函数值
    print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data)

    # 反向传播计算梯度
    f.backward()

    # 如果梯度足够小，则结束迭代
    if a.grad < 0.001:
        break

    # 根据梯度下降规则更新变量值
    a -= a.grad * 0.01
    b -= b.grad * 0.01
    c -= c.grad * 0.01
解释每个部分：

from engine import Value: 导入 Value 类，该类用于构建计算图中的节点。

初始化变量 a、b、c：使用 Value 类初始化三个变量。

while True:: 进入无限循环，即梯度下降的迭代过程。

f = a**2 + b**2 + c**2: 计算目标函数值。

print("a=", a.data, "b=", b.data, "c=", c.data, "f=", f.data): 打印当前变量值和目标函数值。

f.backward(): 执行反向传播，计算目标函数相对于变量 a、b 和 c 的梯度。

if a.grad < 0.001: break: 如果变量 a 的梯度足够小，则结束迭代。

a -= a.grad * 0.01, b -= b.grad * 0.01, c -= c.grad * 0.01: 根据梯度下降规则，更新变量值。

这个循环会一直运行，不断地通过梯度下降来调整变量，使得目标函数逐渐趋近最小值。在每次迭代中，你可以看到变量 a、b、c 和目标函数 f 的当前值。当梯度足够小（即接近零）时，迭代结束。

"""
