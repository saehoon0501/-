N = int(input())

wines = [0]*N
for i in range(N):
    wines[i] = int(input())

sums = [[0]*2 for _ in range(N)]
result = 0
if N == 1:
    sums[0][0] = wines[0]
    sums[0][1] = wines[0]
    result = wines[0]
elif N == 2:
    sums[0][0] = wines[0]
    sums[0][1] = wines[0]
    sums[1][0] = wines[1]
    sums[1][1] = wines[0] + wines[1]
    result = sums[1][1]
else:
    sums[0][0] = wines[0]
    sums[0][1] = wines[0]
    sums[1][0] = wines[1]
    sums[1][1] = wines[0] + wines[1]
    result = sums[1][1]

    for i in range(2,N):
        sums[i][0] = max(max(sums[i-2][0], sums[i-2][1]) + wines[i], max(sums[i-1]))
        sums[i][1] = sums[i-1][0] + wines[i]

        temp = max(sums[i])        
        if temp > result:
            result = temp

print(result)
#포도주 값이 0인 경우를 빼먹었다.