A = int(input())
numbers = list(map(int, input().split()))
dp = [0] * A

dp[0] = numbers[0]
for i in range(1, A):
    dp[i] = numbers[i]
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])
print(max(dp))
