from collections import deque;
import copy;

n = int(input());#보드 크기를 저장한다.
board = [[0 for _ in range(n)] for _ in range(n)];

for i in range(n):
    l = input().split(" ");
    for j in range(len(l)):
        board[i][j] = int(l[j]);

moves = [(1,0), (-1,0), (0,1), (0,-1)]#아래 위 오른쪽 왼쪽 방향을 나타낸다.
queue = deque();
queue.append((board,1));

def bfs(queue, moves):#bfs를 통해 가능한 모든 움직임을 통해 보드를 업데이트한다.
    count = 0;
    ret = 0;

    while len(queue) > 0:#queue 안에는 (보드,카운드)가 저장되어있다.
        board, count = queue.popleft();
        if count > 5:#만약 count가 5가 넘어갔다면 이제부터 계속 넘어갈 것이기에 현재 가장 큰 숫자를 리턴한다.
            return ret;

        for move in moves:#가능한 4가지 움직임을 하나씩 가져와 보드를 업데이트하고 이를 queue에 저장한다.
            newBoard = updateBoard(copy.deepcopy(board), move);
            maxNum = getMax(newBoard);
            if maxNum > ret:#만약 현재 움직임을 업데이트한 보드에서 더 큰 숫자가 나왔다면 이를 리턴 값에 저장한다.
                ret = maxNum;                
            queue.append((newBoard,count+1));
        
    return ret;

def checkMerged(merged, moved):#같은 턴 안에 합쳐지는 것은 1회만 되기에 합쳐진 것들을 확인한 후 이들은 더 이상 합치지 않기 위해 확인한다.
    for d in merged:
        if d == moved:
            return False;

    return True;

def updateBoard(board, move):#움직임마다 index가 보드를 넘어가는지 그리고 0칸이 아닌 다른 칸을 만날때까지 한 방향으로 계속 이동한다.
    n = len(board);
    merged = [];    
    if move == (1,0):#아래로 이동
        for i in range(len(board)-1,-1,-1):            
            for j in range(len(board)):                                
                moved = (i+move[0], j);
                before = (i,j);                                

                while moved[0] <= n-1 and board[moved[0]][moved[1]] == 0:
                    board[moved[0]][moved[1]] = board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    before = moved;
                    moved = (moved[0]+move[0], moved[1]+move[1]);
                
                if moved[0] > n-1:#만약 index가 보드 크기를 넘어가서 움직임을 멈췄다면 바로 다음 칸으로 진행한다.
                    continue;
                #만약 움직임을 통해 같은 칸을 만나서 움직임을 멈춘 경우라면 두 칸을 합치고 합쳐진 칸을 merge에 저장하여 더이상 합쳐지지 않게 한다. 
                if board[moved[0]][moved[1]] == board[before[0]][before[1]] and checkMerged(merged,moved):
                    board[moved[0]][moved[1]] = 2*board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    merged.append(moved);
    
    elif move == (-1,0):#위로 이동
        for i in range(len(board)):
            for j in range(len(board)):
                moved = (i+move[0], j);
                before = (i,j);
                while moved[0] >= 0 and board[(moved[0])][moved[1]] == 0:
                    board[moved[0]][moved[1]] = board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    before = moved;
                    moved = (moved[0]+move[0], moved[1]);
                
                if moved[0] < 0:
                    continue;

                if board[moved[0]][moved[1]] == board[before[0]][before[1]] and checkMerged(merged,moved):
                    board[moved[0]][moved[1]] = 2*board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    merged.append(moved);
                
    elif move == (0,1):#오른쪽으로 이동
        for i in range(len(board)):
            for j in range(len(board)-1, -1,-1):
                moved = (i, j+move[1]);
                before = (i,j);
                while moved[1] <= n-1 and board[(moved[0])][moved[1]] == 0:
                    board[moved[0]][moved[1]] = board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    before = moved;
                    moved = (moved[0], moved[1]+move[1]);
                
                if moved[1] > n-1:
                    continue;

                if board[moved[0]][moved[1]] == board[before[0]][before[1]] and checkMerged(merged,moved):
                    board[moved[0]][moved[1]] = 2*board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    merged.append(moved);
    
    else:#왼쪽으로 이동(0,-1)
        for i in range(len(board)):
            for j in range(len(board)):
                moved = (i, j+move[1]);
                before = (i,j);                        
                while moved[1] >= 0 and board[moved[0]][moved[1]] == 0:                                        
                    board[moved[0]][moved[1]] = board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    before = moved;
                    moved = (moved[0], moved[1]+move[1]);
                                
                if moved[1] < 0:
                    continue;
                
                if board[moved[0]][moved[1]] == board[before[0]][before[1]] and checkMerged(merged,moved):
                    board[moved[0]][moved[1]] = 2*board[before[0]][before[1]];
                    board[before[0]][before[1]] = 0;
                    merged.append(moved);

    return board;

def getMax(board):#현재 보드에서 가장 큰 숫자를 가져와 리턴한다.
    ret = 0;
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] > ret:
                ret = board[i][j]
    
    return ret;

result = bfs(queue, moves);
print(result);