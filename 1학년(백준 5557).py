N = int(input())
numbers = list(map(int, input().split(" ")))
dp = [[0]*21 for _ in range(N-1)]
dp[0][numbers[0]] = 1
for i in range(1,(N-1)):#매 턴
    for j in range(21):#0~20 숫자들
        if dp[i-1][j] != 0:#이전 턴 도달한 횟수가 존재한다면
            if j - numbers[i] >= 0:
                dp[i][j - numbers[i]] += dp[i-1][j]
            if j + numbers[i] <= 20:                
                dp[i][j + numbers[i]] += dp[i-1][j]

print(dp[N-2][numbers[N-1]])