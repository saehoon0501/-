N = int(input())
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    val = int(input())

    dp[i][0] = val
    dp[i][1] = val
    if 0 <= i - 2:
        dp[i][0] += max(dp[i - 2])
    if 0 <= i - 1:
        dp[i][1] += dp[i - 1][0]
        dp[i][2] = max(dp[i - 1])
print(max(dp[-1]))
