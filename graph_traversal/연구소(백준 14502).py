from collections import deque
from copy import deepcopy

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
virus = []
wall = 0
global result
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            virus.append([i, j])
        elif board[i][j] == 1:
            wall += 1
result = 0


def bfs(board):
    dxdy = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    queue = deque(virus)
    count = 0
    while queue:
        vx, vy = queue.popleft()
        for dx, dy in dxdy:
            nx = vx + dx
            ny = vy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    count += 1
                    queue.append([nx, ny])

    return N * M - (wall + len(virus) + count + 3)


def dfs(count):
    global result
    if count == 3:
        result = max(bfs(deepcopy(board)), result)
        return
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visited[i][j]:
                board[i][j] = 1
                visited[i][j] = True
                dfs(count + 1)
                board[i][j] = 0
                visited[i][j] = False
    return


dfs(0)
print(result)
