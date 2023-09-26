from collections import deque

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]


def bfs():
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    horseMove = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [2, -1], [2, 1], [1, -2], [1, 2]]

    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
    q = deque([[0, 0, 0]])
    visited[0][0][0] = 0
    while q:
        i, j, h = q.popleft()

        if i == H - 1 and j == W - 1:
            return visited[i][j][h]

        for dx, dy in dxdy:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][h]:
                if board[nx][ny] == 0:
                    visited[nx][ny][h] = visited[i][j][h] + 1
                    q.append([nx, ny, h])

        if h < K:
            for hx, hy in horseMove:
                nx = i + hx
                ny = j + hy
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][h + 1]:
                    if board[nx][ny] == 0:
                        visited[nx][ny][h + 1] = visited[i][j][h] + 1
                        q.append([nx, ny, h + 1])
    return -1


result = bfs()
if result == -1:
    print(-1)
else:
    print(result)
