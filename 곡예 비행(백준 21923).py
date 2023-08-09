N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]

dp = [[-1e8] * M for _ in range(N)]

# up 과정
for j in range(M):
    for i in range(N - 1, -1, -1):
        if i == N - 1 and j == 0:
            dp[i][j] = board[i][j]
        else:
            if 0 <= i + 1 < N:
                dp[i][j] = max(dp[i][j], dp[i + 1][j])
            if 0 <= j - 1 < M:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
            dp[i][j] += board[i][j]

# down 과정
for j in range(M):
    for i in range(N):
        if i == 0 and j == 0:
            dp[i][j] += board[i][j]
        else:
            if 0 <= i - 1 < N:
                dp[i][j] = max(dp[i][j], dp[i - 1][j])
            if 0 <= j - 1 < M:
                dp[i][j] = max(dp[i][j], dp[i][j - 1])
            dp[i][j] += board[i][j]

print(dp[N - 1][M - 1])
