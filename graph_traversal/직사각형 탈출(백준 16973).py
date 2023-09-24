from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
psum = [[0] * (M + 1) for _ in range(N + 1)]
H, W, Sr, Sc, Fr, Fc = map(int, input().split())
global result
result = 10**7

for i in range(1, N + 1):
    for j in range(1, M + 1):
        psum[i][j] = (
            psum[i - 1][j] + psum[i][j - 1] - psum[i - 1][j - 1] + board[i - 1][j - 1]
        )


def bfs():
    global result
    dxdy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    queue = deque([[Sr - 1, Sc - 1, 0]])
    visited[Sr - 1][Sc - 1] = True

    while queue:
        x, y, count = queue.pop()
        if [x, y] == [Fr - 1, Fc - 1]:
            result = count
            return
        for dx, dy in dxdy:
            if (
                0 <= x + dx < N
                and 0 <= y + dy < M
                and (0 <= x + dx + H - 1 < N)
                and 0 <= y + dy + W - 1 < M
            ):
                if (
                    not (
                        psum[x + dx + H][y + dy + W]
                        - psum[x + dx + H][y + dy]
                        - psum[x + dx][y + dy + W]
                        + psum[x + dx][y + dy]
                    )
                    > 0
                ):
                    if not visited[x + dx][y + dy]:
                        queue.appendleft([x + dx, y + dy, count + 1])
                    visited[x + dx][y + dy] = True
    return


bfs()

if result == 10**7:
    print(-1)
else:
    print(result)

#'최소'를 구하기 위해 한 번 방문한 적이 있는 경우에도 다른 경로를 통해 도달이 가능하면 재방문을 하고 있기 때문에 지수 복잡도가 됩니다.
# BFS는 방문하는 순서 그 자체가 이미 시간순이기 때문에 재방문을 하지 않아도 되고, 그래서 최단 경로를 구하는 데에는 무조건 BFS를 써야 합니다.
# 직사각형 테두리 부분에 벽이 존재하다면 갈 수 없다.
