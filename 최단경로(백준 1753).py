import heapq;
import sys;
INF = sys.maxsize;#정수형 최대값을 사용해 무한대를 표현
input = sys.stdin.readline;#기존 input 함수보다 더 빠르게 입력 받기 위해서 사용한다.

n,m = map(int, input().split(" "));#n은 노드 수 m은 엣지 수
src = int(input());#최단경로 시작 위치를 입력 받는다.
global graph;#그래프를 전역 변수로 사용하기 위해 global 키워드를 사용한다.
graph = {i:[] for i in range(1,n+1)};#dict으로 graph를 표현한다.
pq = [];#최단거리 노드를 가져오기 위한 pq이다.
distance = [INF]*(n+1);#노드들의 최단거리를 저장하는 리스트이다.
visited = [0]*(n+1);#노드가 방문되었는지 기억하기 위한 리스트이다.
distance[src] = 0;#초기 시작 노드의 거리는 0으로 맞춘다.

for _ in range(m):
    u,v,w = map(int, input().split(" "));#u에서 v로 가는 w 가중치 엣지 입력 받는다.
    graph[u].append((v,w));#u에서 v로 가는 가중치 w 방향 엣지를 저장한다.

def updateDistance(distance, src, adjacent):#노드의 최단거리를 업데이트하는 함수이다.
    if distance[adjacent[0]] == INF:#만약 처음으로 거리가 계산되었다면 바로 업데이트 한다.
        distance[adjacent[0]] = (distance[src]+adjacent[1]);
        return;
    
    if distance[adjacent[0]] > (distance[src]+adjacent[1]):#기존에 최단거리가 계산되었다면 더 최단거리를 저장한다.
        distance[adjacent[0]] = (distance[src]+adjacent[1]);
        return;

    return;

def dijkstra(src, pq, visited, distance):
    visited[src] = 1;

    for adjacent in graph[src]:#먼저 시작점 주변 노드들(v,w)에 대해
        updateDistance(distance, src, adjacent);#거리를 업데이트 해준다.
        heapq.heappush(pq, (distance[adjacent[0]], adjacent[0]));#(거리, 노드 번호)로 pq에 저장된다.

    while len(pq) > 0:#결과가 모든 노드에 대해 나올 때까지 반복한다.        
        selected = heapq.heappop(pq);#가장 가까운 거리의 노드를 가져온다.(거리, 노드 번호)
        
        if visited[selected[1]] == 1:#이미 방문되었다면 바로 넘어간다.
            continue;

        visited[selected[1]] = 1;#방문을 표시한다.
        for adjacent in graph[selected[1]]:#그리고 인접 노드들에 대해 
            updateDistance(distance, selected[1], adjacent);#거리를 업데이트 해준다.
            heapq.heappush(pq, (distance[adjacent[0]], adjacent[0]));#(거리, 노드 번호)로 pq에 저장된다.
        
    return;

dijkstra(src,pq,visited,distance);

for i in range(1,n+1):
    if distance[i] == INF:
        print('INF');
    else:
        print(distance[i]);
