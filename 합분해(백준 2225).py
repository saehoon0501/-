N, K = map(int, input().split(" "))
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,(K+1)):
    dp[0][i] = 1

for i in range(1,(N+1)):
    for j in range(1,(K+1)):
        if j == 1:
            dp[i][j] = 1
        else:        
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])

print(dp[-1][K]%1000000000)