N = int(input())
dp = [0] * (5000 + 1)

dp[3] = 1
dp[5] = 1
for i in range(4, N + 1):
    if dp[i - 3] != 0:
        dp[i] = dp[i - 3] + 1

for i in range(10, N + 1):
    if dp[i - 5] != 0:
        dp[i] = dp[i - 5] + 1

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])
