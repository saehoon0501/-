from collections import deque

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(M):
        board[i][j] = int(row[j])

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
q = deque([[0, 0, 0]])
visited[0][0][0] = 1
while q:
    destroyed, i, j = q.popleft()
    if i == N - 1 and j == M - 1:
        break
    for dx, dy in dxdy:
        nx = i + dx
        ny = j + dy
        if 0 <= nx < N and 0 <= ny < M:
            if not destroyed:
                if board[nx][ny] == 1 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[i][j][0] + 1
                    q.append([1, nx, ny])
                elif board[nx][ny] == 0 and not visited[nx][ny][0]:
                    visited[nx][ny][0] = visited[i][j][0] + 1
                    q.append([0, nx, ny])
            else:
                if board[nx][ny] == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = visited[i][j][1] + 1
                    q.append([1, nx, ny])

result = max(visited[N - 1][M - 1])

if result == 0:
    print(-1)
else:
    print(result)
