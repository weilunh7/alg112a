# 方法 1
def power2n_a(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_b(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 2
    elif(n > 1):
        return power2n_b(n-1)+power2n_b(n-1)
    # power2n(n-1)+power2n(n-1)

# 方法2b：用遞迴
def power2n_c(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 2
    elif(n > 1):
        return 2*power2n_c(n-1)
    # 2*power2n(n-1)

# 方法 3：用遞迴+查表
N = [None]*100

def power2n_d(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 2
    if not N[n] is None: return N[n]
    if(n > 1):
        N[n] = power2n_d(n-1)+power2n_d(n-1)
        return N[n]
    # power2n(n-1)+power2n(n-1) 

print(power2n_a(5))
print(power2n_b(5))
print(power2n_c(5))
print(power2n_d(5))

#方法3 參考課程範例 https://github.com/ccc112a/py2cs/blob/master/02-%E6%BC%94%E7%AE%97%E6%B3%95/02-%E6%96%B9%E6%B3%95/01-%E6%9F%A5%E8%A1%A8%E6%B3%95/fiboanacci/fibonacci_lookup.py
