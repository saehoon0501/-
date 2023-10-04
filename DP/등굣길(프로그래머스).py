def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]

    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j + 1, i + 1] not in puddles:
                if j + 1 < m:
                    dp[i][j + 1] += dp[i][j]
                if i + 1 < n:
                    dp[i + 1][j] += dp[i][j]

    answer = dp[n - 1][m - 1] % 1_000_000_007
    return answer
