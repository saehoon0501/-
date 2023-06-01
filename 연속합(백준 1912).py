size = int(input())
sequence = list(map(int, input().split(" ")))
sums = [0]*size
sums[0] = sequence[0]
result = sums[0]
for i in range(1,size):
    sums[i] = max(sequence[i], sums[i-1]+sequence[i])
    if sums[i] > result:
        result = sums[i]

print(result)