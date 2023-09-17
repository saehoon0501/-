N, K = map(int, input().split())
numbers = list(map(int, input().split()))
dp = [[0] * 2 for _ in range(N)]

for i in range(N):
    if numbers[i] % 2 == 0:
        dp[i] = [1, K]

        count = 0
        for j in range(i - 1, -1, -1):
            if K < count:
                break
            if numbers[j] % 2 == 0:
                if count <= dp[j][1]:
                    dp[i][0] += dp[j][0]
                    dp[i][1] = dp[j][1] - count
                    break
                else:
                    dp[i][0] += 1
                    dp[i][1] = K - count
            else:
                count += 1

result = 0
for val, count in dp:
    result = max(result, val)
print(result)
