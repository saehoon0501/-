from collections import deque;
import copy;

def play(board, snake, conditions):
    move = (0,1)#처음 움직임은 오른쪽으로 진행
    count = 0;
    result = True;
    for sec, direction in conditions:#(시간, 방향)으로 방향 전환 조건이 되어있다.
        while count < int(sec) and result:               
            result = moveSnake(snake, board, move);            
            count += 1;

        if count == int(sec):#조건 시간까지 움직임이 다 된 경우 방향을 바꿔준다.
            move = changeDirection(move, direction);
        else:#만약 벽이나 자기 자신에 부딪힌 경우 게임 종료
            return count;

def changeDirection(move, direction):
    if move == (0,1):#기존에 오른쪽인 경우
        if direction == 'D':#오른쪽으로 회전, 아래 방향
            return (1,0);
        
        return (-1,0);

    elif move == (0,-1):#기존에 왼쪽인 경우
        if direction == 'D':#오른쪽으로 회전, 아래 방향
            return (-1,0);
        
        return (1,0);
    elif move == (1,0):#기존에 아래인 경우
        if direction == 'D':#오른쪽으로 회전, 왼쪽 방향
            return (0,-1);
        
        return (0,1);
    else:
        if direction == 'D':#오른쪽으로 회전, 오른쪽 방향
            return (0,1);
        
        return (0,-1);

def moveSnake(snake, board, move):#뱀을 움직여 보드 상 어떤 위치에 뱀과 그 꼬리가 존재하는지 업데이트한다.
    start = snake[0];#뱀 머리 부분을 나타낸다.
    moved = (start[0]+move[0], start[1]+move[1]);#움직인 뱀의 머리를 나타낸다.
    n = len(board);#보드의 크기를 나타낸다.

    if moveOutOfRange(moved, n) and selfTouch(snake, moved):#만약 Index가 보드 내 움직임이고 뱀 꼬리에 뱀이 이동하지 않았다면
        if board[moved[0]][moved[1]] == 1:#움직인 칸에 사과가 존재하면
            snake.appendleft(moved);#움직인 뱀 머리를 가장 앞에 추가하고 길이를 줄이지 않는다.
            board[moved[0]][moved[1]] = 0;#그리고 사과를 없앤다.
        else:#움직인 칸에 사과가 존재하지 않는다면
            snake.appendleft(moved);#뱀 머리를 맨 앞에 추가하고
            snake.pop();#뒤에 있는 꼬리를 줄여준다.
        
        return True
    
    return False;


def moveOutOfRange(moved, n):#움직인 위치가 보드 크기를 넘어선다면 False를 리턴한다.
    if moved[0] <= n-1 and moved[0] >= 0 and moved[1] <= n-1 and moved[1] >= 0:
        return True;

    return False;

def selfTouch(snake, moved):#뱀이 자기 자신이 존재하는 칸에 존재한다면 False를 리턴한다.
    for tail in snake:
        if tail == moved:
            return False;

    return True;

n = int(input());
board = [[0 for _ in range(n)] for _ in range(n)];

k = int(input());

for _ in range(k):
    i, j = map(int, input().split(" "));
    board[i-1][j-1] = 1;

conditions = [];

l = int(input());

for _ in range(l):
    sec, direction = map(str, input().split(" "));
    conditions.append((sec,direction));

conditions.append((10001,'D'));#마지막에 움직임 변경 조건 이후 이를 계속 유지하며 움직이기 위해 움직임 변경 조건에 해당하지 않는 dummy 조건을 넣는다.
snake = deque();
snake.append((0,0));

result = play(board,snake,conditions);
print(result);