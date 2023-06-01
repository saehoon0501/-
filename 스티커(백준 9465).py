def getMax(numbers, dp, row, col):
    maxNum = 0
    start = col - 2

    if col < 2:
        start = 0

    for i in range(2):
        for j in range(start,col):
            if row == i and j == col-1:
                break
            if dp[i][j] > maxNum:
                maxNum = dp[i][j]
    
    dp[row][col] = maxNum + numbers[row][col]
    return dp[row][col]

T = int(input())
ripped = [(0,1), (0,-1), (1,0)]

for _ in range(T):
    N = int(input())    
    numbers = [list(map(int, input().split(" "))) for _ in range(2)]
    dp = [[0]*N for _ in range(2)]
    result = 0
    
    for j in range(N):
        result = max(result, getMax(numbers, dp, 0, j))
        result = max(result, getMax(numbers, dp, 1, j))
    print(result)
