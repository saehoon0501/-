def getSum(start, end, dp):
    startX, startY = start
    endX, endY = end
    ret = dp[endX][endY]
    if startX > 0:
        ret -= dp[startX-1][endY]
    if startY > 0:
        ret -= dp[endX][startY-1]
    if startX > 0 and startY > 0:
        ret += dp[startX-1][startY-1]
    
    return ret

N,M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        dp[i][j] = board[i][j] + dp[i][j-1]

for j in range(M):
    for i in range(N):
        if i>0:
            dp[i][j] += dp[i-1][j]        

K = int(input())
results = []
for _ in range(K):
    startX, startY, endX, endY = map(int, input().split(" "))
    tmp = getSum((startX-1, startY-1), (endX-1, endY-1), dp)
    results.append(tmp)

for r in results:
    print(r)

# 행 부분 합을 구하고 이를 누적하여 열 부분 합을 구하면 (0,0) ~ end 직사각형 합을 구할 수 있다.
# 여기서 뺄 부분을 빼고 중복되게 빠진 부분을 다시 더하면 결과가 빠르게 나온다.