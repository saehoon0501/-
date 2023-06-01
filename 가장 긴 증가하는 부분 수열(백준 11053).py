def getMax(sequence, maxSize, index):    
    maxNum = 0
    
    for i in range(index-1, -1, -1):
        if sequence[i] < sequence[index]:
            if maxSize[i] > maxNum:
                maxNum = maxSize[i]
            
    return maxNum+1

size = int(input())
sequence = list(map(int, input().split(" ")))
maxSize = [1]*size
result = 1

for i in range(1,size):
    maxSize[i] = getMax(sequence, maxSize, i)
    if maxSize[i] > result:
        result = maxSize[i]

print(result)