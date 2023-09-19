T = int(input())
dp = [[0] * 11 for _ in range(11)]

dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 11):
    dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

results = []
for _ in range(T):
    N = int(input())
    results.append(dp[N - 1])

for result in results:
    print(result)
