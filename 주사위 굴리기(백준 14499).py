
def moveDice(dice, move, board, start):#움직임에 따라 주사위를 보드 위에서 움직이고 주사위를 업데이트한다.
    moved = (start[0]+move[0],start[1]+move[1]);

    if indexOut(board, moved):#만약 주사위 이동 위치가 보드를 벗어나면 다 무시하고 초기 위치를 되돌려 리턴한다.
        updateDice(move, dice);#주사위를 업데이트한다.
        num = board[moved[0]][moved[1]];#주사위가 이동한 위치에 보드 칸에 숫자를 가져온다.
        if num == 0:#만약 숫자가 0이라면 보드에 주사위 밑 바닥 숫자를 저장한다.
            board[moved[0]][moved[1]] = dice[4];
        else:#만약 칸에 숫자가 있다면 주사위 밑바닥에 해당 숫자를 넣고 칸은 0으로 바꾼다.
            dice[4] = num;
            board[moved[0]][moved[1]] = 0;
        print(dice[1]);#그리고 주사위를 업데이트할 때마다 주사위에서 가장 윗 부분을 출력한다.
        return moved;#그리고 업데이트한 움직임을 리턴한다.

    return start;

def indexOut(board, moved):#주사위 위치가 보드를 벗어났는지 확인하는 함수이다.
    n = len(board);
    m = len(board[0]);

    if moved[0] <= n-1 and moved[0] >= 0 and moved[1] <= m-1 and moved[1] >= 0:
        return True;
    return False;

def updateDice(move, dice):#주사위 칸 위치마다 숫자를 가지고 주사위 회전 시 움직이는 칸 위치마다 알맞은 순서로 값을 교환한다.
    if move == (1,0):#남쪽으로 이동
        dice[1], dice[2], dice[3], dice[4] = dice[2], dice[4], dice[1], dice[3];
    elif move == (-1,0):#북쪽으로 이동
        dice[1], dice[2], dice[3], dice[4] = dice[3], dice[1], dice[4], dice[2];
    elif move == (0,1):#동쪽으로 이동
        dice[1], dice[4], dice[5], dice[6] = dice[5], dice[6], dice[4], dice[1];
    else:#서쪽으로 이동
        dice[1], dice[4], dice[5], dice[6] = dice[6], dice[5], dice[1], dice[4];

def getMove(order):#이동 명령에 맞춰 2d 배열에서의 움직임을 리턴한다.
    move = 0;
    if order == 4:
        move = (1,0);
    elif order == 3:
        move = (-1,0);
    elif order == 2:
        move = (0,-1);
    else:
        move = (0,1);

    return move;

n,m,x,y,k = map(int, input().split(" "));#n 세로크기, m 가로크기, (x,y) 주사위 놓은 좌표, k 명령의 개수

board = [[0 for _ in range(m)] for _ in range(n)];

for i in range(n):
    l = input().split(" ");
    for j in range(m):
        board[i][j] = int(l[j]);

orders = [];

l = input().split(" ");
for i in range(k):
    orders.append(int(l[i]));

start = (x,y);
dice = {i:0 for i in range(1,7)};

for order in orders:
    move = getMove(order);
    start = moveDice(dice, move, board, start)
    
