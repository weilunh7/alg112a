n = int(input("請輸入數字:"))            
arr = [0,1]                     
for i in range(n-2):           
    if n==0:                
        print(arr[0])
    elif n==1:              
        print(arr)       
    else:                   
        arr.append(arr[i] + arr[i+1])        
print(arr, end=' ') 

#本程式修改至 https://steam.oxxostudio.tw/category/python/example/fibonacci.html
          