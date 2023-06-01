import sys;
from collections import deque;#queue를 사용하기 위한 모듈 import
sys.setrecursionlimit(10**5);

n,m = map(int, input().split(" "));#n은 행의 수 m은 열의 수이다.
board = [['.' for _ in range(m)] for _ in range(n)];#n행 m열에 맞춰 2d 배열의 크기를 설정한다.

red = 0;#빨강 공의 위치를 저장하는 변수
blue = 0;#파랑 공의 위치를 저장하는 변수
holes = [];#정답 위치를 저장한다.
queue = deque();#bfs에서 사용할 queue를 선언한다.

for i in range(n):#먼저 보드의 구성을 입력 받고 R,B,O이면 각 경우 위치를 변수에 맞게 저장해준다.
    l = input();
    for j in range(m):        
        board[i][j] = l[j];
        if l[j] == 'R':
            red = (i,j);
        elif l[j] == 'B':
            blue = (i,j);
        elif l[j] == 'O':
            holes.append((i,j));

moves = [(1,0),(-1,0),(0,1),(0,-1)];#순서대로 아래, 위, 오, 왼

queue.append((red,blue,1));#(빨강 위치, 파랑 위치, 기울인 횟수)를 큐에 저장한다.

def moveBall(ball, secondBall, move, board):#공이 들어오면 이를 움직임 방향으로 갈 수 있을만큼 끝가지 간다.
    ballMoved = (ball[0]+move[0],ball[1]+move[1]);#먼저 공을 움직임 방향에 맞게 한칸 움직인다.
    n = len(board);#보드의 행과 열
    m = len(board[0]);

    if (ballMoved[0] >= n or ballMoved[0] < 0) or (ballMoved[1] >= m or ballMoved[1] < 0):#보드의 행과 열의 크기를 가져와 만약 움직인 칸이 존재하지 않는 경우 바로 기존 공의 위치를 리턴한다.
        return ball;

    #공이 움직인 위치가 막힌 벽이거나 정답 위치이거나 다른 공이 위차한 곳이라면 움직임을 멈춘다. 그 전까지는 움직임 방향으로 계속 이동한다.
    while board[ballMoved[0]][ballMoved[1]] != '#' and board[ballMoved[0]][ballMoved[1]] != 'O' and secondBall != ballMoved:
        ball = ballMoved;
        ballMoved = (ball[0]+move[0],ball[1]+move[1]);
        #만약 움직인 방향이 index out of range인지를 체크해 그렇다면 그 전까지 움직인 공의 위치를 리턴한다.
        if (ballMoved[0] >= n or ballMoved[0] < 0) or (ballMoved[1] >= m or ballMoved[1] < 0):
            return ball;
    #움직임이 끝났는데 정답위치에 도착해서 끝난 경우 움직인 공의 위치를 리턴한다.
    if board[ballMoved[0]][ballMoved[1]] == 'O':
        return ballMoved;
    #그 외의 경우 움직일 수 없는 위치로 움직였기에 기존 공의 위치를 리턴한다.
    return ball;

def updateBoard(red, blue, move, board):#움직임에 맞게 두 공을 보드에서 움직인다. 움직임은 보드는 놔두고 공의 위치 값을 변경하는 것이다.
    #각 진행 방향마다 빨강 공이나 파란 공 중 어느게 먼저 있는지 판단하고 진행 방향에 더 앞에 있는 공을 먼저 움직여야 한다.
    if move == (1,0):#밑으로 기울이기
        if red[0] < blue[0]:#파란 공이 빨강 공 아래 있을 때
            blue = moveBall(blue, red,move, board);
            red = moveBall(red, blue,move, board);
        else:#빨강 공이 파랑 아래 있을 때        
            red = moveBall(red, blue,move,board);
            blue = moveBall(blue, red,move,board);
    elif move == (-1,0):#위로 기울이기
        if red[0] > blue[0]:#파란 공이 빨강 공 위에 있을 때
            blue = moveBall(blue, red,move, board);
            red = moveBall(red, blue,move, board);
        else:#빨강 공이 파랑 위 있을 때        
            red = moveBall(red, blue,move,board);
            blue = moveBall(blue, red,move,board);
    elif move == (0,1):#오른쪽 기울이기
        if red[1] < blue[1]:#파란 공이 빨강 공 오른쪽에 있을 때
            blue = moveBall(blue, red,move, board);
            red = moveBall(red, blue,move, board);
        else:#빨강 공이 파랑 오른쪽 있을 때        
            red = moveBall(red, blue,move,board);
            blue = moveBall(blue, red,move,board);
    else:#왼쪽 기울이기
        if red[1] > blue[1]:#파란 공이 빨강 공 왼쪽에 있을 때
            blue = moveBall(blue, red, move, board);
            red = moveBall(red, blue, move, board);
        else:#빨강 공이 파랑 왼쪽 있을 때        
            red = moveBall(red, blue, move,board);
            blue = moveBall(blue, red, move,board);

    return (red, blue);

def isSolved(ball, holes):#공이 정답 위치에 들어갔는지 확인하는 계산을 한다.
    for answer in holes:
        if ball == answer:
            return True;
    return False;

def bfs(board, moves, red, blue, queue, holes):#queue에는 공의 위치와 기울인 횟수를 저장하고 꺼내면서 공을 움직이고 횟수+1하면서 bfs를 진행한다.    
    count = 1;
    while count < 11 and len(queue) > 0:        
        red, blue, count = queue.popleft();        
        
        for move in moves:
            newRed, newBlue = updateBoard(red, blue, move, board);                       
            if isSolved(newRed, holes) and not isSolved(newBlue, holes):               
                return count;
            #파란 공이 정답 위치에 있으면 그 경우는 더 이상 저장하지 않고 제거해도 되기에 기존 공의 위치가 바꾼 경우와 더불어 조건을 추가한다.
            if (red != newRed or blue != newBlue) and not isSolved(newBlue, holes):
                queue.append((newRed,newBlue, count+1));
    
    return -1;

result = bfs(board, moves, red, blue, queue, holes);
print(result);

        
