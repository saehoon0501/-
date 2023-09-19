N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N
dp[0] = 1
for i in range(1, N):
    dp[i] = 1
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
