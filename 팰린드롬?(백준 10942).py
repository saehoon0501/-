N = int(input())
nums = list(map(int, input().split(" ")))
M = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][1] = 1
for i in range(2, N + 1):
    dp[i][i] = 1
    for j in range(1, i):
        if j < 3:
            if nums[i - j - 1] == nums[i - 1]:
                dp[i - j][i] = 1
        else:
            if nums[i - j - 1] == nums[i - 1] and dp[i - j + 1][i - 1] == 1:
                dp[i - j][i] = 1

results = []
for _ in range(M):
    S, E = map(int, input().split(" "))
    results.append(dp[S][E])

print(*results)
