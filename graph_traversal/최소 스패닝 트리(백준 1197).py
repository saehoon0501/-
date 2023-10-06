from heapq import heappush, heappop

V, E = map(int, input().split())
adjacents = [[] for _ in range(V + 1)]

# edge 구조는 [노드,비용]
for _ in range(E):
    a, b, c = map(int, input().split())
    adjacents[a].append([b, c])
    adjacents[b].append([a, c])

visited = [False] * (V + 1)
heap = []
for node, cost in adjacents[1]:
    heappush(heap, (cost, node))

answer = 0
# 시작 노드 방문처리
visited[1] = True
while heap:
    # 항상 아직 연결되지 않은 노드들을 향하는 엣지 중 가중치가 최소 순서로 가져온다.
    sCost, sNode = heappop(heap)

    # 그리고 아직 연결되지 않은 노드를 향하는 최소 엣지라면 방문 처리 후 결과 업데이트
    # 이미 연결된 노드라면 그냥 패스
    if not visited[sNode]:
        visited[sNode] = True
        answer += sCost
    else:
        continue

    # 인접 노드들 중 아직 연결되지 않은 노드들만 추가
    for adjacent, cost in adjacents[sNode]:
        # 연결된 노드와 인접한 노드들로 향하는 엣지들 중 아직 연결되지 않은 노드에 대해서만 추가한다.
        if not visited[adjacent]:
            heappush(heap, (cost, adjacent))

print(answer)
