def dfs(select, board, dp):    
    moves = [[1,0],[-1,0],[0,1],[0,-1]]
    selectX, selectY = select
    if dp[selectX][selectY] != -1:
        return dp[selectX][selectY]
    if selectX == len(board)-1 and selectY == len(board[0])-1:
        return 1
    
    count = 0
    for dx,dy in moves:
        newSelectX = selectX+dx
        newSelectY = selectY+dy
        if 0<= newSelectX < len(board) and 0<= newSelectY < len(board[0]):
            if board[selectX][selectY] > board[newSelectX][newSelectY]:
                count += dfs([newSelectX,newSelectY], board, dp)
    
    dp[selectX][selectY] = count
    return count


N,M = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

dfs([0,0], board, dp)
print(dp[0][0])
