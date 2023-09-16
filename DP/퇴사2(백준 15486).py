N = int(input())
dp = [0] * (N + 2)

for i in range(1, N + 1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])
    if i + T <= N + 1:
        dp[i + T] = max(dp[i + T], dp[i] + P)
    dp[N + 1] = max(dp[N + 1], dp[N])
print(dp[-1])
