sOne = input()
sTwo = input()

dp = [[0]*(len(sTwo)+1) for _ in range(len(sOne)+1)]

for i in range(1,len(sOne)+1):
    for j in range(1,len(sTwo)+1):        
        if sOne[i-1] == sTwo[j-1]:            
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(sOne)][len(sTwo)])