T = int(input())

results = []

for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0] * (N + 1) for _ in range(M + 1)]

    for j in range(M + 1):
        dp[j][0] = 1

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    results.append(dp[M][N])

for result in results:
    print(result)
