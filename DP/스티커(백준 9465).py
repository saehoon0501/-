T = int(input())
results = []
for _ in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]

    for j in range(N):
        if j == 0:
            dp[0][j] = board[0][j]
            dp[1][j] = board[1][j]
        elif j == 1:
            dp[0][j] = dp[1][j - 1] + board[0][j]
            dp[1][j] = dp[0][j - 1] + board[1][j]
        else:
            dp[0][j] = max(dp[1][j - 2], dp[1][j - 1]) + board[0][j]
            dp[1][j] = max(dp[0][j - 2], dp[0][j - 1]) + board[1][j]

    results.append(max(dp[0][N - 1], dp[1][N - 1]))

for result in results:
    print(result)
