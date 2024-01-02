import numpy as np
import time
 
#calculate gradient
def cal_gradient(A, b, x):
    left = np.dot(np.dot(A.T, A), x)
    right = np.dot(A.T, b)
    gradient = left - right
    return gradient
 
# iteration
def gradient_decent(x, A, b, learning_rate, step):
    start = time.time()
    for i in range(step):
        gradient = cal_gradient(A, b, x)
        delta = learning_rate * gradient
        x = x - delta
    end = time.time()
    time_cost = round(end - start, 4)
    print('done! x = {a}, time cost = {b}s'.format(a=x, b=time_cost))

A = np.array([[1.0, -2.0, 1.0], [0.0, 2.0, -8.0], [-4.0, 5.0, 9.0]])
b = np.array([0.0, 8.0, -9.0])
# Giveb A and b，the solution x is [29, 16, 3]
 
x0 = np.array([1.0, 1.0, 1.0])
learning_rate = 0.01
step = 1000000
 
gradient_decent(x0, A, b, learning_rate, step)

#程式來源 :　https://blog.csdn.net/u010960155/article/details/113776715
#相關資訊 : https://ithelp.ithome.com.tw/articles/10327491?sc=rss.iron
