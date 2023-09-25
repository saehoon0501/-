from collections import deque

N, K = map(int, input().split())
visited = [False] * (100_001)


def bfs():
    moves = [-1, 1]
    queue = deque([[N, 0]])
    visited[N] = True

    while queue:
        pos, count = queue.popleft()
        if pos == K:
            return count
        if 0 <= 2 * pos < 100_001 and not visited[2 * pos]:
            visited[2 * pos] = True
            queue.appendleft([2 * pos, count])
        for m in moves:
            if 0 <= pos + m < 100_001 and not visited[m + pos]:
                visited[m + pos] = True
                queue.append([m + pos, count + 1])

    return 0


result = bfs()
print(result)

# 2*pos는 count가 증가하지 않기에 큐 맨 앞에 넣어서 count 시점을 모두 동일하게 가져가는 bfs에 맞게 한다.
# -1을 1보다 먼저 처리하여야 N 이전 값들도 2*pos에 영향을 받을 수 있게된다.
