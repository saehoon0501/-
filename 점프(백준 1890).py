def getMax(board, dp, row, col, N):
    print(dp)
    if board[row][col] == 0:
        return

    newRow = row + board[row][col]
    newCol = col + board[row][col]    
    if 0<= newRow < N:
        dp[newRow][col] = dp[row][col] + 1
        getMax(board, dp, newRow, col, N)
    if 0<= newCol < N:
        dp[row][newCol] = dp[row][col] + 1
        getMax(board, dp, row, newCol, N)
    
N = int(input())
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        newRow = i + board[i][j]
        newCol = j + board[i][j]
        if 0<= newRow < N:
            dp[newRow][j] += dp[i][j]
        if 0<= newCol < N:
            dp[i][newCol] += dp[i][j]

print(dp[N-1][N-1])