from numpy import arange

def f(x):
    return x**2-3*x+1

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001: 
        print("x=", x, " f(x)=", f(x)) 

f1 = lambda x:(x**2+1)/3
f2 = lambda x:(3*x-1)**0.5
f3 = lambda x:(x-1)**2


x1 = x2 = x3 = 1

for i in range(20):
    x1, x2 , x3= f1(x1), f2(x2), f3(x3)
    print('x1:', x1, 'x2:', x2, 'x3:', x3)
