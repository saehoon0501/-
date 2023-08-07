N, M = map(int, input().split(" "))
numbers = []
sums = [0] * (N + 1)
for i in range(1, N + 1):
    num = int(input())
    numbers.append(num)
    sums[i] = sums[i - 1] + num

dp = [[0] + [-1e9] * (M) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, min(M, (i // 2) + 1) + 1):
        dp[i][j] = dp[i - 1][j]

        for k in range(1, i + 1):
            if j == 1 and k == 1:
                dp[i][j] = max(dp[i][j], sums[i])
            else:
                if k - 2 >= ((j - 1) * 2) - 1:
                    dp[i][j] = max(dp[i][j], dp[k - 2][j - 1] + sums[i] - sums[k - 1])

print(dp[N][M])
