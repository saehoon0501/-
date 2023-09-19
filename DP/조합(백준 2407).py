N, M = map(int, input().split())
dp = [[0] * M for _ in range(N)]

for i in range(N):
    dp[i][0] = i + 1

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

print(dp[N - 1][M - 1])
