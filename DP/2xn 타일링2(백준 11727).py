N = int(input())
dp = [0] * 1000
dp[0] = 1
# 1 인 경우를 고려하지 않음
if 2 <= N:
    dp[1] = 3
for i in range(2, N):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[N - 1] % 10007)
