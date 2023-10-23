N, K = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [[0] * (K + 1) for _ in range(N)]

if numbers[0] % 2 == 0:
    dp[0][0] = 1


for i in range(1, N):
    if numbers[i] % 2 == 0:
        dp[i][0] = 1
        for j in range(min(i, K + 1)):
            dp[i][j] = dp[i - 1][j] + 1
    else:
        for j in range(min(i, K + 1)):
            if j + 1 < K + 1:
                dp[i][j + 1] = dp[i - 1][j]

result = 0
for r in dp:
    result = max(result, max(r))
print(result)
