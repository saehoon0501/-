from collections import deque

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
hasSword_visited = [[False] * M for _ in range(N)]


def bfs():
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([[0, 0, False, 0]])
    visited[0][0] = True
    if board[0][0] == 2:
        queue = deque([[0, 0, True, 0]])

    while queue:
        x, y, hasSword, count = queue.popleft()
        if count > T:
            continue
        if x == N - 1 and y == M - 1:
            return count
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if hasSword:
                if 0 <= nx < N and 0 <= ny < M and not hasSword_visited[nx][ny]:
                    hasSword_visited[nx][ny] = True
                    queue.append([nx, ny, hasSword, count + 1])
            else:
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                    if board[nx][ny] == 0:
                        visited[nx][ny] = True
                        queue.append([nx, ny, hasSword, count + 1])
                    elif board[nx][ny] == 2:
                        visited[nx][ny] = True
                        queue.append([nx, ny, True, count + 1])

    return -1


result = bfs()
if result == -1:
    print("Fail")
else:
    print(result)

# 칼을 먹은 경우 기존에 갔던 곳들도 다시 가봐야 정답을 구할 수 있다.
