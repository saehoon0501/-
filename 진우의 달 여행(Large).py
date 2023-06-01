N,M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
INF = float('inf')
dp = [[[INF]*3 for _ in range(M)] for _ in range(N)]

for j in range(M):    
    dp[0][j][0] = board[0][j]
    dp[0][j][1] = board[0][j]
    dp[0][j][2] = board[0][j]

for i in range(1,N):
    for j in range(M):
        if j-1 >= 0:
            dp[i][j][0] = min(dp[i-1][j-1][2], dp[i-1][j-1][1]) + board[i][j]        
        if j+1 <= M-1:
            dp[i][j][2] = min(dp[i-1][j+1][1], dp[i-1][j+1][0]) + board[i][j]
        dp[i][j][1] = min(dp[i-1][j][2], dp[i-1][j][0]) + board[i][j]

answer = INF
for i in range(M):
    answer = min(min(dp[N-1][i]), answer)

print(answer)
#3D 배열을 만들 때 for문 2개로 사용해야한다 마지막만 []*숫자 구문 사용