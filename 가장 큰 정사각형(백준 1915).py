n, m = map(int, input().split(" "))
board = [list(map(int, input())) for _ in range(n)]
moves = [[0, -1], [-1, -1], [-1, 0]]
dp = [board[i][0:] for i in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            tmp = 1e9
            for dx, dy in moves:
                if 0 <= i + dx < n and 0 <= j + dy < m:
                    if dp[i + dx][j + dy] >= 1:
                        tmp = min(tmp, dp[i + dx][j + dy])
                    else:
                        tmp = 0
                        break
                else:
                    tmp = 0
                    break
            dp[i][j] += tmp
            result = max(result, dp[i][j])

print(result**2)
