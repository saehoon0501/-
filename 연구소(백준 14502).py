from collections import deque;
import copy;

def bfs(graph, queue):
    dxdy = [(0,1),(0,-1),(1,0),(-1,0)];

    while(queue):
        row, col = queue.popleft();
        for infection in dxdy:
                x, y = infection;
                tmpX = row+x;
                tmpY = col+y;
                if tmpX < 0 or tmpX >= n or tmpY < 0 or tmpY >= m:
                    continue;
                if graph[tmpX][tmpY] == 0:
                    graph[tmpX][tmpY] = 2;
                    queue.append((tmpX,tmpY));
    counter = 0;
    for line in graph:
        counter += line.count(0);

    return counter;

def makeWall(graph, queue, count):
    answer = 0;
    if count == 3:
        answer = bfs(copy.deepcopy(graph), copy.deepcopy(queue));
        return answer;

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1;
                answer = max(answer,makeWall(graph, queue, count+1));
                graph[i][j] = 0;

    return answer;

if __name__ == '__main__':
    n, m = map(int, input().split(" "));
    graph = [];
    queue = deque();

    for i in range(n):
        graph.append(list(map(int,input().split(" "))));
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i,j));

    print(makeWall(copy.deepcopy(graph), queue, 0));

# 파리미터로 넘기는 변수가 함수 내에서 값이 변하면 원본 변수에도 영향을 미치는지 정확히 확인
# index array out of bound 조건 확인
