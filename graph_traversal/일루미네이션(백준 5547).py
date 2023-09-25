from collections import deque

W, H = map(int, input().split())
board = [[0] * (W + 2) for _ in range(H + 2)]
visited = [[False] * (W + 2) for _ in range(H + 2)]

for i in range(1, H + 1):
    row = list(map(int, input().split()))
    for j in range(1, W + 1):
        board[i][j] = row[j - 1]

count = 0
odddxdy = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]
evendxdy = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]

queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()
    if x % 2 == 0:
        for dx, dy in evendxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H + 2 and 0 <= ny < W + 2:
                if board[nx][ny] == 1:
                    count += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])
    else:
        for dx, dy in odddxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H + 2 and 0 <= ny < W + 2:
                if board[nx][ny] == 1:
                    count += 1
                elif not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append([nx, ny])

print(count)
