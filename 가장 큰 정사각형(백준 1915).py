n,m = map(int, input().split(" "))
board = [[0]*m for _ in range(n)]
dp = [[0]*m for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(m):
        board[i][j] = int(row[j])

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = board[i][j]
        elif board[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1],dp[i][j-1]) + 1

answer = 0
for i in range(n):
    answer = max(max(dp[i]), answer)
print(answer*answer)