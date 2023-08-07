m, n = map(int, input().split(" "))

board = [list(map(int, input().split(" "))) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]


def dfs(sx, sy):
    dxdy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    if dp[sx][sy] != -1:
        return dp[sx][sy]
    if sx == m - 1 and sy == n - 1:
        return 1
    dp[sx][sy] = 0
    currentVal = board[sx][sy]
    for dx, dy in dxdy:
        if 0 <= sx + dx < m and 0 <= sy + dy < n:
            if currentVal > board[sx + dx][sy + dy]:
                dp[sx][sy] += dfs(sx + dx, sy + dy)

    return dp[sx][sy]


print(dfs(0, 0))
