N = int(input())
edge = [0 for _ in range(N)]
visited = [False] * N
for i in range(N):
    to = int(input())
    edge[i] = to - 1

global goal
global result
global picked
result = 0
goal = 0
picked = []


def dfs(start, nodes, count):
    global result
    global picked
    if count != 0 and start == goal:
        visited[goal] = True
        result += count
        for n in nodes:
            picked.append(n)
        return 1
    adjacent = edge[start]
    if not visited[adjacent]:
        visited[adjacent] = True
        nodes.append(adjacent)
        if dfs(adjacent, nodes, count + 1) == 0:
            visited[adjacent] = False
    return 0


for i in range(N):
    goal = i
    if edge[i] == i:
        picked.append(i)
        result += 1
        continue
    dfs(i, [], 0)

picked.sort()

print(result)
for p in picked:
    print(p + 1)
