from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
results = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]


def bfs(start):
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    q = deque([start])
    visited[start[0]][start[1]] = True
    count = 1
    zeros = set()
    while q:
        i, j = q.popleft()
        for dx, dy in dxdy:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    count += 1
                elif board[nx][ny] == 0:
                    if (nx, ny) not in zeros:
                        zeros.add((nx, ny))
    for i, j in zeros:
        results[i][j] += count
    return


for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            bfs([i, j])

result = 0
for i in range(N):
    for j in range(M):
        result = max(result, results[i][j])
print(result + 1)
