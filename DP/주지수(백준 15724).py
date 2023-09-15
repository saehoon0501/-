N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if j == 0:
            dp[i][j] = board[i][j]
        else:
            dp[i][j] = dp[i][j - 1] + board[i][j]

for i in range(1, N):
    for j in range(M):
        dp[i][j] += dp[i - 1][j]

K = int(input())
results = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2 - 1][y2 - 1]
    if y1 != 1:
        result -= dp[x2 - 1][y1 - 2]
    if x1 != 1:
        result -= dp[x1 - 2][y2 - 1]
    if y1 != 1 and x1 != 1:
        result += dp[x1 - 2][y1 - 2]

    results.append(result)

for result in results:
    print(result)
