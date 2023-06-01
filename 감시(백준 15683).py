import copy;
#주어진 CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구한다.
#CCTV는 서로를 통과해 감시할 수 있다. 최대 개수는 8개 이다.

n,m = map(int, input().split(" "));
board = [list(map(int, input().split(" "))) for _ in range(n)];
cams = [];

for i in range(n):
    for j in range(m):
        if 0 < board[i][j] < 6:
            cams.append((i,j, board[i][j]));

cams.sort(key=lambda x:(-x[2]));

def findMinBlindSpot(board, cams):
    ret = 0;

    for c in cams:
        coverMaxSpace(board, c);

    for row in board:
        ret += row.count(0);

    return ret;

def coverMaxSpace(board, c):    
    x,y = c[0], c[1];    
    
    if board[x][y] == 1:
        moves = [[(0,1)],[(0,-1)],[(1,0)],[(-1,0)]];#오,왼,아래,위
        cover(c, board, moves);
    
    elif board[x][y] == 2:
        moves = [[(0,1),(0,-1)],[(1,0),(-1,0)]];#오&왼,아래&위        
        cover(c, board, moves);

    elif board[x][y] == 3:
        moves = [[(0,1),(-1,0)],[(1,0),(0,1)],[(1,0),(0,-1)],[(0,-1),(-1,0)]];#오&위,아래&오,아래&왼,왼&위
        cover(c, board, moves);

    elif board[x][y] == 4:
        moves = [[(0,-1),(-1,0),(0,1)],[(-1,0),(0,1),(1,0)],#왼&위&오,위&오&아래
                 [(0,1),(1,0),(0,-1)],[(1,0),(0,-1),(-1,0)]];#오&아래&왼,아래&왼&위
        cover(c, board, moves);
    else:#5번 카메라
        moves = [[(0,-1),(-1,0),(0,1), (1,0)]];
        cover(c, board, moves);

def cover(start, board, moves):
    maxCover = 0;
    selected = [];

    for m in moves:
        count = 0;
        for direction in m:
            dx, dy = start[0]+direction[0], start[1]+direction[1];
            if indexOut(dx,dy,len(board), len(board[0])):
                continue;
            while -1<= board[dx][dy] < 6:
                if board[dx][dy] == 0:
                    count += 1;
                dx, dy = dx+direction[0], dy+direction[1];
                if indexOut(dx,dy,len(board), len(board[0])):
                    break;
        if maxCover < count:
            maxCover = count;
            selected = m;

    for direction in selected:
        dx, dy = start[0]+direction[0], start[1]+direction[1];
        if indexOut(dx,dy,len(board), len(board[0])):
                continue;
        while -1<= board[dx][dy] < 6:
            if board[dx][dy] == 0:
                board[dx][dy] = -1;
            dx, dy = dx+direction[0], dy+direction[1];

            if indexOut(dx,dy,len(board), len(board[0])):
                break;

def indexOut(x,y,n,m):
    if x < 0 or x >= n:
        return True;
    if y <0 or y >= m:
        return True;
    return False;

result = n*m;
start = 0;
tmp = [];

for i in range(len(cams)):    
    if cams[i][2] != 5:
        start = i;
        tmp = cams[0:i];
        break;

stack = [];

def shuffle(stack, tmp, cams, start, n):
    if len(tmp) == n:
        stack.append(tmp);
        return;

    for i in range(start, len(cams)):
        tmp.append(cams[i]);
        val = cams.pop(i);
        shuffle(stack, copy.deepcopy(tmp), copy.deepcopy(cams), start, n);
        tmp.pop();
        cams.insert(i, val);

shuffle(stack, tmp, cams, start, len(cams));

while len(stack) > 0:
    cams = stack.pop();
    result = min(result,findMinBlindSpot(copy.deepcopy(board), cams));

print(result);