N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[[1e9] * 3 for _ in range(M)] for _ in range(N)]

dp[0] = [[board[0][i], board[0][i], board[0][i]] for i in range(M)]

moves = [[-1, -1], [-1, 0], [-1, 1]]
for i in range(1, N):
    for j in range(M):
        for k in range(3):
            dx, dy = moves[k]
            if 0 <= i + dx < N and 0 <= j + dy < M:
                if k == 0:
                    dp[i][j][k] = (
                        min(dp[i + dx][j + dy][1], dp[i + dx][j + dy][2]) + board[i][j]
                    )
                elif k == 1:
                    dp[i][j][k] = (
                        min(dp[i + dx][j + dy][0], dp[i + dx][j + dy][2]) + board[i][j]
                    )
                else:
                    dp[i][j][k] = (
                        min(dp[i + dx][j + dy][0], dp[i + dx][j + dy][1]) + board[i][j]
                    )

result = 1e9
for i in range(M):
    result = min(min(dp[N - 1][i]), result)

print(result)
