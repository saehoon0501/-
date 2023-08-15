N, M, H = map(int, input().split(" "))
dp = [[0] * 1001 for _ in range(N + 1)]
blocks = [list(map(int, input().split(" "))) for _ in range(N)]
dp[0][0] = 1
for i in range(1, N + 1):
    dp[i] = dp[i - 1][0:]
    for b in blocks[i - 1]:
        for j in range(b, H + 1):
            dp[i][j] += dp[i - 1][j - b]

print(dp[N][H] % 10007)
