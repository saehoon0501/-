T = int(input())

results = []
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    amount = int(input())
    dp = [1] + [0] * (amount)

    for c in coins:
        for i in range(amount + 1):
            if i + c <= amount:
                dp[i + c] += dp[i]
            else:
                break
    results.append(dp[amount])

for result in results:
    print(result)
