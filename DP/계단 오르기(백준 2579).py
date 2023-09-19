N = int(input())
dp = [[0] * 2 for _ in range(N)]

for i in range(N):
    step = int(input())

    dp[i][0] = step
    dp[i][1] = step
    if 0 <= i - 1:
        dp[i][0] += dp[i - 1][1]
    if 0 <= i - 2:
        dp[i][1] += max(dp[i - 2])

print(max(dp[N - 1]))
