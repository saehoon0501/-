N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]


answer = 10**7
for i in range(3):
    dp = [[10**7] * 3 for _ in range(N)]
    dp[0][i] = costs[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + costs[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + costs[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + costs[j][2]
    dp[N - 1][i] = 10**7

    answer = min(answer, min(dp[N - 1]))

print(answer)
