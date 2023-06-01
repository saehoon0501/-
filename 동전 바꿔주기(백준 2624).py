T = int(input())
k = int(input())
coin = [[0, 0]]
dp = [[0 for _ in range(T+1)] for _ in range(k+1)]
for _ in range(k):
    x, y = map(int, input().split())
    coin.append([x, y])

dp[0][0] = 1
for i in range(1, k+1):
    val, cnt = coin[i]
    for j in range(T+1):
        dp[i][j] = dp[i-1][j]
        for v in range(1, cnt+1):
            if j-v*val >= 0:
                dp[i][j] += dp[i-1][j-v*val]
            else:
                break

print(dp)
print(dp[k][T])