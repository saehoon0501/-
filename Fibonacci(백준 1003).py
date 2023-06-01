def fibonacci(array, n):    
    array[0] = (1,0);
    array[1] = (0, 1);
    for i in range(2,n+1):
         zeroCount = array[(i-1)%3][0] + array[(i-2)%3][0];
         oneCount = array[(i-1)%3][1] + array[(i-2)%3][1];
         array[i%3] = (zeroCount, oneCount);
    
    return array[n%3];

size = int(input());

array = {};
result = [];

for i in range(3):
    array[i] = (0,0);

for i in range(size):
    n = int(input());
    result.append(fibonacci(array, n));

for x in result:
    print(x[0], x[1]);