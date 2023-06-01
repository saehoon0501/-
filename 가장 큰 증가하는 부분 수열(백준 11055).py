def getMax(sequence, sums, index):
    maxNum = 0

    for i in range(index-1, -1, -1):
        if sequence[i] < sequence[index] and sums[i] > maxNum:
            maxNum = sums[i]

    return maxNum + sequence[index]

size = int(input())
sequence = list(map(int, input().split(" ")))
sums = [0]*size
sums[0] = sequence[0]

for i in range(1,size):
    sums[i] = max(sequence[i], getMax(sequence, sums, i))

print(max(sums))