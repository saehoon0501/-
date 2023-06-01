def getSum(sums, start, end):
    ret = 0
    x1,y1 = start
    x2,y2 = end
    
    for i in range(x1,x2+1):
        if y1 == 0:
            ret += sums[i][y2]
        else:            
            ret += sums[i][y2] - sums[i][y1-1]
    
    return ret

N, M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
sums = [[0]*(N) for _ in range(N)]
sums[0][0] = board[0][0]

for i in range(N):
    for j in range(N):
        if j == 0:
            sums[i][j] = board[i][j]
        else:
            sums[i][j] = sums[i][j-1] + board[i][j]

results = []
for _ in range(M):
    x1,y1,x2,y2 = map(int, input().split(" "))
    results.append(getSum(sums, (x1-1,y1-1), (x2-1,y2-1)))

for result in results:
    print(result)