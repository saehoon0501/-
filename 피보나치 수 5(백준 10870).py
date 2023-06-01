def fibo(n, array):
    if n == 0:
        array[0] = 0
    
    if n >= 1:
        array[0] = 0
        array[1] = 1
        
    for i in range(2,n+1):
        array[i] = array[i-1] + array[i-2]
    
number = int(input())
array = [0]*(number+1)


fibo(number, array)
print(array[number])