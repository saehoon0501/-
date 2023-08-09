N = int(input())
weighs = list(map(int, input().split(" ")))

totalWeigh = sum(weighs)

M = int(input())
sphere = list(map(int, input().split(" ")))

dp = [[0] * (totalWeigh + 1) for _ in range(N)]
dp[0][weighs[0]] = 1
results = []
for i in range(1, N):
    dp[i][weighs[i]] = 1
    for j in range(1, totalWeigh + 1):
        if dp[i - 1][j] == 1:
            dp[i][j] = 1
            if (j + weighs[i]) <= totalWeigh:
                dp[i][j + weighs[i]] = 1

for s in sphere:
    if s <= totalWeigh:
        if dp[N - 1][s] == 1:
            results.append("Y")
        else:
            for j in range(1, totalWeigh + 1):
                if dp[N - 1][j] == 1 and j + s <= totalWeigh:
                    if dp[N - 1][j + s] == 1:
                        results.append("Y")
                        break
                elif j + s > totalWeigh:
                    results.append("N")
                    break
    else:
        results.append("N")

print(*results)
