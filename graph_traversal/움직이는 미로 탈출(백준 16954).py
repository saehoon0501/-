from collections import deque

board = []
global wall
wall = set()

for i in range(8):
    row = input()
    board.append(row)

for i in range(8):
    for j in range(8):
        if board[i][j] == "#":
            wall.add((i, j))


def bfs():
    global wall
    dxdy = [
        [0, 0],
        [1, 0],
        [1, 1],
        [1, -1],
        [0, 1],
        [0, -1],
        [-1, 0],
        [-1, -1],
        [-1, 1],
    ]
    q = deque([[7, 0]])
    visited = [[False] * 8 for _ in range(8)]
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if (i, j) in wall:
                continue

            if i == 0 and j == 7:
                return 1

            for dx, dy in dxdy:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < 8 and 0 <= ny < 8:
                    if not visited[nx][ny] and (nx, ny) not in wall:
                        visited[nx][ny] = True
                        q.append([nx, ny])
        visited = [[False] * 8 for _ in range(8)]
        new_wall = set()
        for i, j in wall:
            new_wall.add((i + 1, j))
        wall = new_wall
    return 0


print(bfs())

# 매 턴마다 움직임을 제어하기 위해 for loop에 현재 존재하는 q의 크기만큼 반복한다.
# 한 턴씩 차례차례 생각하면 쉽게 해결 가능
