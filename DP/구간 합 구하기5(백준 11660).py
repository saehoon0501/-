N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]


for i in range(N):
    for j in range(N):
        if j == 0:
            dp[i][j] = board[i][j]
        else:
            dp[i][j] = dp[i][j - 1] + board[i][j]

for j in range(N):
    for i in range(1, N):
        dp[i][j] += dp[i - 1][j]

results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    result = dp[x2 - 1][y2 - 1]

    if 0 <= y1 - 2:
        result -= dp[x2 - 1][y1 - 2]
    if 0 <= x1 - 2:
        result -= dp[x1 - 2][y2 - 1]
    if 0 <= x1 - 2 and 0 <= y1 - 2:
        result += dp[x1 - 2][y1 - 2]
    results.append(result)

for r in results:
    print(r)
