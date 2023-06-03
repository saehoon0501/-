N = int(input())
numbers = list(map(int, input().split(" ")))
M = int(input())
dp = [[-1]*N for _ in range(N)]

for length in range(N):
    for i in range(N):
        if i+length >= N:
            break
        if length == 0:
            dp[i][i+length] = 1
        elif length == 1:
            if numbers[i] == numbers[i+length]:
                dp[i][i+length] = 1
            else:
                dp[i][i+length] = 0
        else:
            if numbers[i] == numbers[i+length]:
                if dp[i+1][i+length-1] == 1:
                    dp[i][i+length] = 1
                else:
                    dp[i][i+length] = 0
            else:
                dp[i][i+length] = 0
        
results = []
for _ in range(M):
    start,length = map(int, input().split(" "))
    results.append(dp[start-1][length-1])
for r in results:
    print(r)