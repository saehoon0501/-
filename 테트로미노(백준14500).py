import copy;
import sys;

input = sys.stdin.readline;
n,m = map(int, input().split(" "));
board = [];

for _ in range(n):        
    board.append(list(map(int, input().split(" "))));

stack = [];
global maxNum;
maxNum = 0;
maxElement = max([max(i) for i in board]);

def dfs(board, stack, start, maxElement):
    global maxNum;
    count = 0;
    moves = [(1,0), (-1,0), (0,1), (0,-1)];
    ㅗ_shape = [
        ((0, 1), (0, 2), (1, 1)),
        ((0, 1), (0, 2), (-1, 1)),
        ((-1, 0), (-2, 0), (-1, 1)),
        ((-1, 0), (-2, 0), (-1, -1)),
        ((0, -1), (0, -2), (1, -1)),
        ((0, -1), (0, -2), (-1, -1)),
        ((1, 0), (2, 0), (1, 1)),
        ((1, 0), (2, 0), (1, -1)),
    ];
    n = len(board);
    m = len(board[0]);

    while len(stack) > 0:
        tectro, sum, count = stack.pop();                
        if count < 4:
            for move in moves:
                s = tectro[-1];
                moved = (s[0]+move[0],s[1]+move[1]);
                if moved[0] > n-1 or moved[0] < 0 or moved[1] > m-1 or moved[1] < 0:
                    continue;
            
                if isTectro(moved,tectro) and maxNum < sum + (maxElement*(4-count)):
                    tectro.append(moved);
                    stack.append((copy.deepcopy(tectro), sum+board[moved[0]][moved[1]], count+1));
                    tectro.pop();
        else:            
            maxNum = max(maxNum, sum);
    
    for ㅗ in ㅗ_shape:        
        sum = board[start[0]][start[1]];
        for dy, dx in ㅗ:            
            moved = (start[0]+dx, start[1]+dy);            
            if moved[0] > n-1 or moved[0] < 0 or moved[1] > m-1 or moved[1] < 0:                
                sum = board[start[0]][start[1]];
                break;
            sum = sum+board[moved[0]][moved[1]];                        
                
        if maxNum < sum:
            maxNum = sum;

    return;

def isTectro(coord, tectro):
    for square in tectro:
        if square == coord:            
            return False;

    return True;

for i in range(n):
    for j in range(m):        
        stack.append(([(i,j)],board[i][j],1));
        dfs(board, stack, (i,j), maxElement);
        
print(maxNum);