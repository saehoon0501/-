N = int(input())
numbers = list(map(int, input().split()))
dp = [0] * N

dp[0] = numbers[0]
for i in range(1, N):
    if numbers[i] < dp[i - 1] + numbers[i]:
        dp[i] = dp[i - 1] + numbers[i]
    else:
        dp[i] = numbers[i]

print(max(dp))
