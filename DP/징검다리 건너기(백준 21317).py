N = int(input())
dp = [[10**6] * 2 for _ in range(N)]
steps = [list(map(int, input().split())) for _ in range(N - 1)]
K = int(input())

dp[0][0] = 0
for i in range(N - 1):
    small, medium = steps[i]

    if i + 1 < N:
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + small)
    if i + 2 < N:
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + medium)
    if i + 3 < N:
        dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + K)
    if dp[i][1] != 10**6:
        if i + 1 < N:
            dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + small)
        if i + 2 < N:
            dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + medium)
print(min(dp[-1]))

# 딱 한번 할 수 있는 수퍼 점프가 반영되면 이전에 했던 이후 모든 결과들을 수정해줘야한다
# 이유는 점화식으로 구한 결과들은 1,2 칸에서 움직임만을 고려했기에 3칸 움직임이 반영되면 기존 결과가 싹다 바뀌기 때문
