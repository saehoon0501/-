def getMax(sequence, evens, index, count, length):
    if index < 0:
        return length
    if count <= 0 and sequence[index] % 2 != 0:
        return length
    if evens[index][count] != 0:
        return evens[index][count] + length
    
    value = 0
    if sequence[index] % 2 == 0:
        value = getMax(sequence, evens, index-1, count, length+1)
    else:
        value = getMax(sequence, evens, index-1, count-1, length)
    
    evens[index][count] = value
    return evens[index][count]

N,K = map(int, input().split(" "))
sequence = list(map(int, input().split(" ")))
evens = [[0]*(K+1) for _ in range(N)]
result = 0
for i in range(N):    
    if sequence[i] % 2 == 0:
        result = max(result, getMax(sequence, evens, i, K, 0))

print(result)