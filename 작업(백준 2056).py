N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    tmps = list(map(int, input().split(" ")))
    consumed_time = tmps[0]
    numberOfDep = tmps[1]

    if i == 1:
        dp[i] = consumed_time
    else:
        for j in range(numberOfDep):
            dp[i] = max(dp[i], dp[tmps[j + 2]])
        dp[i] += consumed_time

print(max(dp))
