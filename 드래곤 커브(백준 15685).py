
#드래곤 커브의 개수 n 입력 받음
n = int(input());
#각 드래곤 커브의 정보를 입력 받음 x,y,d,g (x,y)는 시작 점, d는 시작 방향, g는 세대
curves = [list(map(int, input().split(" "))) for _ in range(n)];
#d = 0는 right , d = 1은 up, d = 2는 left, d = 3은 down
#격자는 100x100 사이즈로 2d 배열을 사용한다.
board = [[0]*101 for _ in range(101)];
#각 정보에 맞게 드래곤 커브를 생성하고 각 점의 좌표에 따라 격자에 1로 표시한다. 그리고 점들의 정보를 다 저장한다.
def markCurve(start, direction, gen, dots):    
    dots.append((start[0], start[1]));
    directions = [];
    directions.append(direction);

    while gen > 0:
        tmp = [];
        for i in range(len(directions)-1, -1, -1):
            nd = cw(directions[i]);
            tmp.append(nd);
        for nd in tmp:
            directions.append(nd);        
        gen = gen - 1;

    for d in directions:
        move = getMove(d);
        start = (start[0]+move[0], start[1]+move[1]);
        if 0 <= start[0] < 101 and 0 <= start[1] < 101:
            dots.append(start);

def cw(d):
    if d == 0:
        return 1;
    elif d == 1:
        return 2;
    elif d == 2:
        return 3;
    else:
        return 0;

def getMove(d):
    if d == 0:
        return (0,1);
    elif d == 1:
        return (-1,0);
    elif d == 2:
        return (0,-1);
    else:
        return (1,0);

dots = [];
for x,y,d,g in curves:    
    markCurve((y,x), d, g, dots);

#격자에서 가장 왼쪽 아래에 있는 점이 가장 먼저 오게 저장된 점들의 정보를 배열하고 한 점마다 사각형이 있는지 찾는 시퀀스를 돌린다.
dots.sort(key=lambda x:(x[1],-x[0]));

count = 0;
while count < len(dots):
    x,y = dots[count];

    if board[x][y] == 0:
        board[x][y] = 1;
        count += 1;
        continue;
    if board[x][y] == 1:
        dots.pop(count);

# 모든 점마다 가장 왼쪽아래에 있는 시작점이라 가정하고 오른쪽 위쪽 오른쪽위 대각선쪽 이렇게 3가지 방향의 점들이 모두 1이면 카운트+1

def countSquares(board, dot):
    moves = [(0,1), (-1,0), (0,-1)];
    for m in moves:
        dot = (dot[0]+m[0], dot[1]+m[1]);    
        if 0 > dot[0] or dot[0] >= 101 or 0 > dot[1] or dot[1] >= 101:
            return 0;
        if board[dot[0]][dot[1]] != 1:
            return 0;
    return 1;
count = 0;

for dot in dots:
    count += countSquares(board, dot);

#모든 실행이 끝나면 카운트 출력 후 종료한다.
print(count);