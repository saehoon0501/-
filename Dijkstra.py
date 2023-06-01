import sys;#int 타입의 최대값을 가져오기 위해 모듈 사용한다.

class PQ:#Priority Queue를 Heap 구조로 구현한다.
    def __init__(self, edgeSize):#Priority Queue 생성자이다.
        self.queue = [(0,0) for _ in range(edgeSize)];#PQ에서 데이터를 저장한 배열로 엣지=(노드,가중치)를 저장한다.
        self.count = 0;#PQ에서 저장되는 데이터의 수를 저장한다. 이를 이용해 데이터를 관리한다.
    
    def insert(self,edge):#PQ에서 데이터를 추가할 때 사용한다.
        self.count += 1;#먼저 카운터를 +1로 업데이트 한다.
        self.queue[self.count] = edge;#그 다음 Heap 가장 끝자리에 엣지를 추가한다.
        index = self.count;#추가된 데이터의 index를 저장한다.

        if self.count == 1:#만약 데이터가 하나만 존재한다면 크기를 비교해 부모와 자식 관계를 유지할 필요가 없기에 바로 리턴한다.
            return;

        while(self.queue[int(index/2)][1] > self.queue[index][1]):#실수한 부분 [1]을 까먹어서 weight끼리 비교를 놓침, 현재 추가된 노드의 부모와 크기를 비교해 부모의 가중치가 더 작을 때까지 자리교환을 반복한다.
            temp = self.queue[int(index/2)];#부모 노드를 임시 저장한다.
            self.queue[int(index/2)] = self.queue[index];#자식 노드를 부모 노드 자리에 넣는다.
            self.queue[index] = temp;#자식 노드 자리에 부모 노드를 넣는다.
            index = int(index/2);#자리교환이 된 후 부모 노드로 간 노드의 위치에서 부모 노드와 다시 비교를 위해 index를 업데이트한다.
        return;
        
    def delete(self):#PQ에서 가장 최소 가중치 엣지를 하나 pop하기 위한 함수이다.
        ret = self.queue[1];#루트 노드는 항상 가장 최소를 가지기에 이를 리턴하기 위해 임시저장한다.
        self.queue[1] = self.queue[self.count];#그리고 가장 끝에 위치한 노드를 루트 위치에 넣는다.
        self.count -= 1;#기존 루트 노드는 빼왓기에 카운트 -1로 업데이트한다.

        parent = 1;#parent 실수 self.count가 아니라 1을 넣어야함
        leftChild = parent * 2;#루트 노드가 가지는 왼쪽 자식 노드 Index
        rightChild = parent * 2 + 1;#루트 노드가 가지는 오른쪽 자식 노드 Index

        while(True):#python은 True를 써야함, 루트 노드를 pop한 이후 다시 관계를 유지하는 Heap 구조를 유지하기 위해 부모,자식 노드간 비교를 통한 자리교환이다.
            if self.count >= rightChild:#이 순서대로 해야 만약 부모와 자식 중 제일 작은 노드가 값이 같아도 무한 루프에 빠지지 않는다.
                if self.queue[leftChild][1] < self.queue[rightChild][1]:
                    if self.queue[parent][1] > self.queue[leftChild][1]:#부모 노드가 왼쪽 자식 노드 보다 더 작고 오른쪽 자식 노드는 아닐 경우와 두 자식노드보다 작지만 왼쪽 노드가 더 작은 경우                    
                        temp = self.queue[parent];#부모노드를 임시저장한다.
                        self.queue[parent] = self.queue[leftChild];#왼쪽 자식 노드를 부모 노드 위치로 이동
                        self.queue[leftChild] = temp;#왼쪽 자식 노드로 부모 노드가 이동
                        parent = leftChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 왼쪽 자식 노드로 업데이트
                    else:#만약 부모 노드가 자식 노드와 값이 동일하거나 더 작으면 빠져 나온다.
                        break;
                else:
                    if self.queue[parent][1] > self.queue[rightChild][1]:#부모 노드가 오른쪽 노드보다 더 작거나 두 자식 노드보다 더 작지만 이 중 오른쪽 자식 노드가 더 작은 경우
                        temp = self.queue[parent];#부모노드를 임시저장한다.
                        self.queue[parent] = self.queue[rightChild];#오른쪽 자식 노드를 부모 노드 위치로 이동
                        self.queue[rightChild] = temp;#오른쪽 자식 노드로 부모 노드가 이동
                        parent = rightChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 오른쪽 자식 노드로 업데이트
                    else:#만약 부모 노드가 자식 노드와 값이 동일하거나 더 작으면 빠져 나온다.
                        break;
            elif self.count >= leftChild:#만약 부모 노드가 자식 노드를 하나만 가지는 경우 Heap 구조 상 항상 왼쪽 자식 노드만 가진다.
                if self.queue[leftChild][1] < self.queue[parent][1]:#부모 노드가 자식 노드보다 더 큰 경우
                        temp = self.queue[parent];#부모노드를 임시저장한다.
                        self.queue[parent] = self.queue[leftChild];#왼쪽 자식 노드를 부모 노드 위치로 이동
                        self.queue[leftChild] = temp;#왼쪽 자식 노드로 부모 노드가 이동
                        parent = leftChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 왼쪽 자식 노드로 업데이트
                else:#만약 부모 노드가 관계를 유지 또는 값이 동일한 경우 빠져 나온다.
                    break;
            else:#자식 노드가 없는 경우 빠져 나온다.
                break;
        
            leftChild = parent * 2;# 실수한 부분 parent에 맞춰 자식 index를 업데이트하는 것을 까먹음 그리고 indent 실수로 while문 밖에 존재했음
            rightChild = parent * 2 + 1;
        
        return ret;#루트 노드 값을 리턴한다.(가장 최소 가중치를 가진다.)

def updateDistance(distance, src):#각 노드의 src로부터 거리를 업데이트하는 함수이다. 거리는 이전 노드의 거리 + 가중치 의 값과 기존 distance에 존재했던 거리 비교를 통해 더 작은게 저장된다.
    global graph;#그래프를 가져온다.

    for node in graph[src].keys():#노드와 adjacent한 노드 번호를 가져온다.
        if distance[node-1] == sys.maxsize:#만약 해당 노드의 거리가 무한대인 경우 처음으로 접근이 가능해졌다는 의미이다.
            distance[node-1] = distance[src-1] + graph[src][node];#바로 이전 노드 거리 + 가중치로 업데이트 한다.
        else:#만약 해당 노드의 거리가 이전에 업데이터가 되었던 경우라면
            if distance[node-1] > distance[src-1] + graph[src][node]:#그리고 그 거리보다 더 작은 거리를의 경로를 찾았다면
                distance[node-1] = distance[src-1] + graph[src][node];#더 작은 거리로 업데이트 한다.


if __name__ == "__main__":
    global graph;
    graph = {};#그래프는 이중 dict구조를 통해 표현한다. 두 번째 dict은 초기화 때 들어간다.

    n, m = map(int, input().split(" "));#n은 노드의 수, m은 엣지들의 수
    src = int(input());#Dijkstra의 시작 노드 번호를 저장한다.

    pq = PQ(m);#엣지 수 만큼 queue의 크기를 할당한다.

    for i in range(n):#그래프를 노드 번호만큼 초기화 한다.
        graph[i+1] = {};#graph는 key는 노드번호 value는 Dictionary를 가진다.(이 Dict은 key 인접노드 번호, value 가중치를 가진다.)

    for i in range(m):#엣지 수 만큼 읽어드려 그래프에 반영한다.
        node, connectedNode, weight = map(int,input().split(" "));#실수한 부분 map을 사용해 인자를 나눠 할당하는걸 놓침
        graph[node][connectedNode] = weight;#graph[node]는 {}를 의미하고 여기에 key로 connectedNode, value로 weight를 넣는다.
        # graph[connectedNode][node] = weight; Dijkstra의 경우 방향 그래프에서만 따진다.
    
    mark = [0 for _ in range(n+1)];#실수한 부분 0 for _ in range(n+1)에서 for _를 빠뜨림, 노드의 최단거리가 이미 반영되었는지 확인하기 위한 배열이다.
    distance = [sys.maxsize for _ in range(n)]; #정수형의 최댓값을 상수로 쓰기 위해서는 sys를 import해야 한다. sys.maxint는 maxsize로 변경됨(python3 기준)
    shortestPath = [src];#최단거리가 짧은 순으로 노드가 저장된다.
    
    distance[src-1] = 0;#시작 노드 번호 -1로 해야 해당 index가 나온다. 이를 통해 시작 노드의 거리는 0으로 세팅한다.
    mark[src-1] = 1;#시작 노드는 최단거리가 0임으로 반영되었다고 체크를 해준다.

    #update adjacent node by distance from node src
    for node in graph[src].keys():#시작 노드와 인접한 노드들을 가져온다.
        weight = graph[src][node];#시작 노드와 인접한 노드를 연결하는 엣지의 가중치를 저장한다.
        distance[node-1] = weight;#그리고 시작 노드와 인접한 노드들의 거리를 업데이트한다. 이전 노드 거리는 0에서 시작하기에 가중치만 반영하면된다.

    for i in range(len(distance)):#그리고 이렇게 반영된 거리들을 pq에 넣어 O(nlogn)의 성능으로 최소값을 찾는다.
        pq.insert((i+1,distance[i]));#pq에 넣는다.

    while(len(shortestPath) < n):#조건이 n까지 가야되는데 ==을 써서 바로 나오게 함
        #pop lowest distance
        closestNode = pq.delete();            
        #check if node is already marked
        #if it is just skip it and get another node from pq
        if mark[closestNode[0]] == 1:
            continue;
        #if not mark it and update adjacent node
        mark[closestNode[0]] = 1;
        updateDistance(distance, closestNode[0]);
        #push node into shortestPath
        shortestPath.append(closestNode[0]);
        #clear pq and push updated value into pq
        pq = PQ(m);#pq를 초기화할 때 배열 자체를 초기화하면 []로 되어 count랑 맞춰지지도 않고 크기도 없어진다 그냥 새로 생성하는게 좋을듯
        for i in range(len(distance)):#queue를 초기화했으니 이제 업데이트된 distance 값들로 다시 채워 다음 최솟값을 찾아본다.
            pq.insert((i+1,distance[i]));

    for d in distance:#최단 거리 값들을 가져와 노드 번호 오름차순으로 출력하고 접근 불가한 노드의 경우 INF를 출력한다.
        if d == sys.maxsize:
            print("INF");
            continue;
        print(d);