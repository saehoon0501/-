C, N = map(int, input().split())
dp = [10**6] * (C + 101)

for _ in range(N):
    cost, customer = map(int, input().split())

    dp[customer] = min(dp[customer], cost)
    for j in range(customer + 1, C + 101):
        if dp[j - customer] != 10**6:
            dp[j] = min(dp[j], dp[j - customer] + cost)
print(min(dp[C:]))
