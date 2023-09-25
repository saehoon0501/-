N, M = map(int, input().split())
relationship = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    relationship[a].append(b)
    relationship[b].append(a)


def dfs(start, nodes, count):
    if count == 5:
        return 1
    visited[start] = True
    for friend in relationship[start]:
        if not visited[friend]:
            nodes.append(friend)
            result = dfs(friend, nodes, count + 1)
            nodes.pop()
            if result == 1:
                return 1
    visited[start] = False
    return 0


for i in range(N):
    result = dfs(i, [i], 1)
    if result == 1:
        break

if result == 0:
    print(0)
else:
    print(1)

# 친구들을 노드 관계를 엣지로 생각하자.
