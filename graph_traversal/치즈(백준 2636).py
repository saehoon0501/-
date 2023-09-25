from collections import deque

N, M = map(int, input().split())
global cheese
cheese = [list(map(int, input().split())) for _ in range(N)]


def bfs(melted):
    global cheese
    count = 0
    visited = [[False] * M for _ in range(N)]
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([[0, 0]])
    visited[0][0] = True

    while queue:
        x, y = queue.pop()
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if melted[nx][ny] == 1:
                    count += 1
                    cheese[nx][ny] = 0
                else:
                    queue.append([nx, ny])
                visited[nx][ny] = True
    return count


result = 0
for i in range(N):
    for j in range(M):
        if cheese[i][j] == 1:
            result = 1
            break

if result == 0:
    print(0)
    print(0)
else:
    result = 0
    i = 0
    while True:
        i += 1
        count = bfs(cheese[0:])
        if count == 0:
            break
        result = count

    print(i - 1)
    print(result)
