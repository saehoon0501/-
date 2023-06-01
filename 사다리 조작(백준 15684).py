
#세로선을 타고 h만큼 내려갔을 때 자기 자신에서 끝나는 경우를 만들기 위한 추가하는 가로선의 최소 개수를 구한다.
n,m,h = map(int, input().split(" "));#세로선 수 n, 가로선 수 m, 가로선을 놓을 수 있는 위치 개수 h
lines = {i:[i for _ in range(h)] for i in range(1,n+1)};
global ret;
ret = 4;

for _ in range(m):
    a,b = map(int, input().split(" "));#a는 점선의 위치, b는 b와 b+1 세로선 사이에 가로선이 존재함을 의미한다.
    lines[b][a-1] = b+1;
    lines[b+1][a-1] = b;

def play(lines, h):    
    for i in range(1, len(lines)+1):
        step = 0;
        switchedLine = i;
    
        while step < h:
            switchedLine = lines[switchedLine][step];
            step += 1;

        if i != switchedLine:
            return False;
    
    return True;

def dfs(lines, h, added, col, row):
    global ret;    
    
    if play(lines, h):
        if added < ret:
            ret = added;
        return;                        

    if added == 3:
        return;
    
    for i in range(col, len(lines)):
        if i != col:
            row = 0;
        for j in range(row, h):
            if lines[i][j] == i and lines[i+1][j] == i+1:
                lines[i][j] = i+1;
                lines[i+1][j] = i;
                dfs(lines, h, added+1, i, j+1); 
                lines[i][j] = i;
                lines[i+1][j] = i+1;

    return;

dfs(lines, h, 0, 1, 0);
if ret <= 3:
    print(ret)
else:
    print(-1);
