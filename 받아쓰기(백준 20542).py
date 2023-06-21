N,M = map(int, input().split(" "))
written = input()
answer = input()
dp = [[i]+[0]*M for i in range(N+1)]

for j in range(M+1):
    dp[0][j] = j

for i in range(1,N+1):
    for j in range(1,M+1):        
        if written[i-1] == answer[j-1]:
            dp[i][j] = dp[i-1][j-1]
        elif written[i-1] == 'v' and answer[j-1] == 'w':                    
            dp[i][j] = dp[i-1][j-1]
        elif written[i-1] == 'i' and (answer[j-1] == 'j' or answer[j-1] == 'l'):
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

print(dp[N][M])