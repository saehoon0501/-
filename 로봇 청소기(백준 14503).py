

n,m = map(int, input().split(" "));
startPos = list(map(int, input().split(" ")));
board = [list(map(int, input().split(" "))) for _ in range(n)];

def clean(board, startPos):
    move = getDirection(startPos);#시작 방향값을 가져온다.
    pos = (startPos[0], startPos[1]);
    count = 0;
    n = len(board);
    m = len(board[0]);

    while True:        
        if board[pos[0]][pos[1]] == 0:#현재 칸 청소되지 않은 경우 현재 칸을 청소한다.
            board[pos[0]][pos[1]] = 2;
            count += 1;
            continue;
        
        if searchForUncleaned(pos, board):#주변 4칸 중 청소되지 않은 칸이 존재하는 경우
            move = rotate90(move);#청소되지 않은 칸이 나올 때까지 반시계 90도 회전한다.
            if indexOut(n,m,(pos[0]+move[0],pos[1]+move[1])):
                continue;
            elif board[pos[0]+move[0]][pos[1]+move[1]] == 0:
                pos = (pos[0]+move[0],pos[1]+move[1]);#그리고 방향 앞쪽 칸이 0이면 전진한다.

        else:#주변 4칸 중 청소되지 않은 칸이 없는 경우            
            pos = (pos[0]-move[0],pos[1]-move[1]);#방향 유지 1칸 후진한다.
            if indexOut(n,m,pos) or isWall(pos, board):#만약 막혀있다면
                return count;

def getDirection(startPos):
    if startPos[2] == 0:#북쪽
        return (-1,0);
    elif startPos[2] == 1:#동쪽
        return (0,1);
    elif startPos[2] == 2:#남쪽
        return (1,0);
    else:#서쪽
        return (0,-1);

def searchForUncleaned(pos,board):
    moves = [(-1,0),(1,0),(0,1),(0,-1)];

    for move in moves:
        moved = (pos[0]+move[0], pos[1]+move[1]);
        if indexOut(len(board), len(board[0]), moved):
            continue;
        
        if board[moved[0]][moved[1]] == 0:
            return True;
    
    return False;

def rotate90(move):
    if move == (-1,0):#북쪽 -> 서쪽
        return (0,-1);
    elif move == (1,0):#남쪽 -> 동쪽
        return (0,1);
    elif move == (0,1):#동쪽 -> 북쪽
        return (-1,0);
    else:#서쪽 -> 남쪽
        return (1,0);

def indexOut(n,m,pos):
    if pos[0] < 0 or pos[0] >= n or pos[1] >=m or pos[1] < 0:
        return True;
    return False;

def isWall(pos, board):
    if board[pos[0]][pos[1]] == 1:
        return True;
    return False;

result = clean(board, startPos);
print(result);