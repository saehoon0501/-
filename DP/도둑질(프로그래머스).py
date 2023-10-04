def solution(money):
    answer = 0
    INF = 1001

    for i in range(2):
        dp = [[0] * 2 for _ in range(len(money))]
        # 시작 집을 턴 경우
        if i == 0:
            dp[0][1] = money[0]

        for j in range(1, len(money)):
            dp[j][0] = max(dp[j - 1])
            dp[j][1] = dp[j - 1][0] + money[j]
        if i == 0:
            dp[len(money) - 1][1] = -INF

        answer = max(answer, max(dp[len(money) - 1]))

    return answer
