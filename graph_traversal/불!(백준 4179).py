from collections import deque

R, C = map(int, input().split())
visited = [[False] * C for _ in range(R)]
board = []
fire = []
pos = []
for _ in range(R):
    row = input().rstrip()
    board.append(row)

for i in range(R):
    for j in range(C):
        if board[i][j] == "F":
            fire.append([i, j])
            visited[i][j] = True
        elif board[i][j] == "J":
            pos = [i, j]


def bfs():
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 불의 위치를 먼저 J 위치를 나중으로 q 초기화
    q = deque([])
    for i, j in fire:
        q.append(["F", i, j, 0])
    q.append(["J", pos[0], pos[1], 0])
    Jcount = 1
    while q:
        item, i, j, count = q.popleft()
        if Jcount <= 0:
            return -1

        if item == "F":
            for dx, dy in dxdy:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if board[nx][ny] != "#":
                        visited[nx][ny] = True
                        q.append(["F", nx, ny, 0])
        else:
            Jcount -= 1
            if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                return count + 1
            for dx, dy in dxdy:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if board[nx][ny] == ".":
                        q.append(["J", nx, ny, count + 1])
                        visited[nx][ny] = True
                        Jcount += 1
    return -1


result = bfs()
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)

# J가 없지는 것 보다 큐 안에 내용이 없는지 먼저 체크하는 조건이 있기에 bfs 자체 return -1도 필요함
# J가 움직이는 곳도 visited 처리해줘도 됨. 왜냐하면 J는 이전에 갔던 칸을 다시 돌아가야할 시나리오가 없어서
