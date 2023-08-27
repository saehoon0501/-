T = int(input())
k = int(input())

dp = [[0] * (T + 1) for _ in range(k + 1)]

for i in range(1, k + 1):
    p, n = map(int, input().split())

    dp[i] = dp[i - 1][:]
    for l in range(1, n + 1):
        val = l * p

        for j in range(1, T + 1 - val):
            if dp[i - 1][j] >= 1 and j + val <= T:
                dp[i][j + val] += dp[i - 1][j]
        if val <= T:
            dp[i][val] += 1

print(dp[-1][-1])
