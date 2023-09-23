from collections import deque

N, M = map(int, input().split())
board = [[] for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(M):
        board[i].append(int(row[j]))


def bfs():
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    queue = deque([[0, 0, 1]])

    result = 10**5
    while len(queue) > 0:
        x, y, sum = queue.pop()
        if x == N - 1 and y == M - 1:
            result = min(result, sum)
            continue
        for dx, dy in dxdy:
            if 0 <= x + dx < N and 0 <= y + dy < M:
                if board[x + dx][y + dy] == 1 and visited[x + dx][y + dy] == False:
                    queue.appendleft([x + dx, y + dy, sum + 1])
                    visited[x + dx][y + dy] = True
    return result


print(bfs())
