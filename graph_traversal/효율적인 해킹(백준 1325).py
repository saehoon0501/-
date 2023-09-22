from collections import deque

N, M = map(int, input().split())
adjacents = [[] for _ in range(N + 1)]
hack_count = [0] * (N + 1)

for _ in range(M):
    adjacent, node = map(int, input().split())
    adjacents[node].append(adjacent)


def bfs(start):
    result = 0
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    while len(queue) > 0:
        node = queue.pop()
        for adjacent in adjacents[node]:
            if visited[adjacent] == False:
                result += 1
                visited[adjacent] = True
                queue.appendleft(adjacent)
    return result


for i in range(1, N + 1):
    hack_count[i] = bfs(i)

result = max(hack_count)
results = []
for i in range(1, N + 1):
    if hack_count[i] == result:
        results.append(i)

print(*results)

# 사이클의 경우 고려해야함
# 이렇게 많은 연산을 수행하는 경우 재귀 dfs로 풀 경우 시간 초과 남
# 구현 방식에서 bfs가 재귀 dfs보다 성능이 좋기 때문에 둘 다 사용할 수 있으면 bfs를 사용하자.
