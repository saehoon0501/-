import heapq;#heap을 위해 사용하는 모듈이다.

n = int(input());#n = 노드 수
m = int(input());#m = 엣지 수

pq = [];#heap을 위한 리스트이다.

for _ in range(m):#엣지 수 만큼 입력을 받는다.
    a,b,c = map(int,input().split(" "));#노드 a,b와 연결되는 엣지 가중치가 c이다.  
    heapq.heappush(pq,(c,a,b));#가중치를 기준으로 엣지를 정렬해야 하기에 모든 엣지를 heap에 저장한다.

visited = [i for i in range(n+1)];#노드의 집합 union을 통해 cycle을 발견하기 위해 사용하는 리스트이다.

def getMST(visited, pq):#최소 가중치 트리를 찾기 위한 내용이다.
    ret = [];#mst를 위해 연결되는 엣지들을 저장하기 위한 리스트이다.
    while len(ret) < n-1:#모든 노드가 연결되기 위해 n-1개의 엣지가 선택되면 된다.
        c,a,b= heapq.heappop(pq);#가중치가 작은 순으로 엣지들을 가져온다.
        if checkCycle(visited,a,b):#만약 엣지가 cycle을 만들지 않는다면 추가한다.
            union(visited,a,b);#추가된 후 연결된 노드 간 집합을 일치시킨다.
            ret.append((a,b,c));#그리고 엣지를 추가한다.
    
    return ret;

def checkCycle(visited, a, b):#싸이클을 체크하기 위한 함수이다.
    aParent = getParent(visited, a);#노드 a가 속한 집합을 찾는다. 이를 위해 집합의 parent를 가져온다.
    bParent = getParent(visited, b);#노드 b가 속한 집합을 찾는다.

    if aParent == bParent:#만약 두 노드가 같은 집합이라면 싸이클을 이루기에 False를 리턴한다.
        return False;

    return True;#아닐 경우 True를 리턴한다.

def getParent(visited, a):#노드가 속한 집합을 가져온다. 이를 위해 노드의 부모 노드를 가져와 집합을 확인한다.
    if visited[a] == a:#만약 노드가 집합의 부모 노드라면 해당 노드를 리턴한다.
        return a;
    return getParent(visited, visited[a]);#아닐 경우 부모 노드를 찾을 때까지 부모 노드를 찾아간다.

def union(visited, a, b):#노드가 서로 연결될 때 같은 집합으로 합치는 연산을 한다.
    aParent = getParent(visited,a);#노드 a의 부모 노드를 가져온다.
    bParent = getParent(visited,b);#노드 b의 부모 노드를 가져온다.
    
    visited[bParent] = aParent;#노드 b의 집합을 a 집합에 속하게 하여 두 집합을 합친다.

result = getMST(visited,pq);#MST 결과 선택된 엣지들을 가져온다.
sum = 0;#그리고 그 가중치들의 총합을 구한다.
for a,b,c in result:#저장된 튜플들을 나눈다.
    sum += c;#그 중 가중치만 합에 추가한다.

print(sum)# 가중치를 출력한다.