R, C, N = map(int, input().split())
board = [[*input()] for _ in range(R)]


def fill():
    results = []
    for i in range(R):
        for j in range(C):
            if board[i][j] == "O":
                results.append([i, j])
            else:
                board[i][j] = "O"
    return results


def boom(prev):
    dxdy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i, j in prev:
        board[i][j] = "."
        for dx, dy in dxdy:
            nx, ny = i + dx, j + dy
            if 0 <= nx < R and 0 <= ny < C:
                board[nx][ny] = "."
    return


sec = 1
prev = []
while sec < N:
    sec += 1
    if sec % 2 == 0:
        prev = fill()
    elif sec % 2 == 1:
        boom(prev)

for row in board:
    result = ""
    for c in row:
        result += c
    print(result)
