N,M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = board[0][0]

for j in range(M):
    for i in range(N-1, -1, -1):
        if j != 0:
            if i != N-1:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])+board[i][j]
            else:
                dp[i][j] = dp[i][j-1]+board[i][j]
        else:
            if i != N-1:
                dp[i][j] = dp[i+1][j] + board[i][j]
            else:
                dp[i][j] = board[i][j]

for i in range(N):
    for j in range(M):
        if j != 0:
            if i != 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i][j]) + board[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i][j]) + board[i][j]
        else:
            if i != 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j]) + board[i][j]
            else:
                dp[i][j] += board[i][j]

print(dp[N-1][M-1])