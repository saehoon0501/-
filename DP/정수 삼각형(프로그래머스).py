def solution(triangle):
    answer = 0
    dp = [[] for _ in range(501)]

    for idx, level in enumerate(triangle):
        dp[idx + 1] = [0] * (len(level))
    dp[1][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(len(dp[i])):
            dp[i + 1][j] = max(dp[i][j] + triangle[i][j], dp[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i][j] + triangle[i][j + 1], dp[i + 1][j + 1])

    answer = max(dp[len(triangle)])
    return answer
