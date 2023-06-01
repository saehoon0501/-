N = int(input())
dp = [[0]*10 for _ in range(N)]

for i in range(1,10):
    dp[0][i] = 1

for n in range(1,N):
    for j in range(10):
        if j == 0:
            dp[n][j] = dp[n-1][j+1]
        elif j == 9:
            dp[n][j] = dp[n-1][j-1]
        else:
            dp[n][j] = dp[n-1][j-1] + dp[n-1][j+1]

result = 0
for i in range(10):
    result += dp[N-1][i]
print(result % 1_000_000_000)