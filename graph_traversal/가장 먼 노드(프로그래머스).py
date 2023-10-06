from collections import deque


def solution(n, edge):
    answer = 0

    # 간선들을 저장
    adjacents = [[] for _ in range(n + 1)]
    for a, b in edge:
        adjacents[a].append(b)
        adjacents[b].append(a)

    # 각 노드들의 거리 값들 초기화
    distance = [-1] * (n + 1)

    # bfs 진행
    bfs(distance, adjacents)

    # 업데이트된 거리 값 중 최대 값을 가져온다.
    result = max(distance)

    for d in distance:
        if d == result:
            answer += 1

    return answer


def bfs(distance, adjacents):
    # 시작 노드 1로 큐 초기화, 거리 값 초기화
    q = deque([1])
    distance[1] = 0

    # 큐가 비어있을 때까지
    while q:
        # 노드를 가져온다.
        node = q.popleft()

        # 해당 노드와 인접한 노드들 중 거리값이 아직 갱신되지 않은 노드들만 접근한다.
        for adjacent in adjacents[node]:
            if distance[adjacent] == -1:
                distance[adjacent] = distance[node] + 1
                q.append(adjacent)
    return
