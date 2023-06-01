import copy;
from collections import deque;

n, m = map(int, input().split(" "));
map = [list(map(int, input().split(" "))) for _ in range(n)];
chicken = [];
house = [];

for i in range(n):
    for j in range(n):
        if map[i][j] == 2:
            chicken.append((i,j));
        elif map[i][j] == 1:
            house.append((i,j));

def bfs(m, chicken, house):
    queue = deque();
    queue.append(([], 0));
    minimum= 0;

    while len(queue) > 0:
        selected, count = queue.popleft();

        if count == 0:
            for i in range(len(chicken)-m+1):
                selected.append(i);
                queue.append((copy.deepcopy(selected), count+1));
                selected.pop();
            continue;
        
        if count == m:            
            ret = getChickenDistance(selected, chicken, house);
            if minimum == 0 or ret < minimum:
                minimum = ret;
            continue;
        
        for i in range(selected[count-1]+1,len(chicken)):
            selected.append(i);
            queue.append((copy.deepcopy(selected), count+1));
            selected.pop();

    return minimum;

def getChickenDistance(selected, chicken, house):
    ret = 0;    
    for h in house:
        closest = 0;
        for s in selected:
            chickPos = chicken[s];
            tmp = abs(h[0] - chickPos[0]) + abs(h[1] - chickPos[1]);
            if closest == 0 or tmp < closest:
                closest = tmp;
        ret += closest;        
    
    return ret;

result = bfs(m, chicken, house);
print(result);