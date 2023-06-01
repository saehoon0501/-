class PQ:
    def __init__(self): # PQ의 Constructor
        self.queue = [(0,0) for _ in range(100_000)];#queue를 100개의 (0,0) 크기로 세팅
        self.count = 0;#queue에 들어가는 item의 수를 세기 위한 counter 변수
    
    def insert(self, edge): #queue에 item을 추가하는 기능
        self.count+= 1; #먼저 counter를 +1 업데이트한다.
        self.queue[self.count] = edge; # 이후 counter를 index로 하여 queue에 edge를 추가한다. 
        index = self.count; #따라서 index는 1부터 시작한다.

        if self.count == 1:#만약 count가 1이라면 추가한 후 Heap 구조를 위한 비교할 대상이 없기에 바로 종료한다.
            return;
        
        while self.queue[int(index/2)][1] > edge[1]:#비교할 대상이 있다면 추가된 자리의 부모 노드와 가중치 값을 비교해 더 작을 때까지 자리교환한다.
            temp = self.queue[int(index/2)];#자리를 교환하기 위해 먼저 부모 노드 값을 임시로 저장한다.
            self.queue[int(index/2)] = edge;#부모 노드 자리에 자식 노드를 넣는다.
            self.queue[index] = temp;# 자식 노드 자리에 임시 저장된 부모 노드를 넣는다.
            index = int(index / 2);#자리교환 이후 다시 부모 노드와 자식 노드 간 관계를 비교하기 위해 index를 업데이트한다.
        #자식 노드 간의 크기는 상관없고 단지 부모 노드와 자식 노드간 관계를 유지하기 위해 동작함을 유의한다.
        return;# 부모와 자식간 관계정리가 끝나면 자리교환을 마치고 while문을 빠져나와 종료한다.
    
    def delete(self):#queue에 저장된 값 중 가장 작은 root 노드 값을 빼온 후 부모 자식 관계를 다시 맞추는 기능이다.
        ret = self.queue[1];#먼저 Root 노드 값을 임시 저장한다.
        self.queue[1] = self.queue[self.count];#가장 끝자리에 있는 노드를 Root 노드 위치로 이동한다.
        self.count-= 1;# 카운트를 -1 업데이트한다. 어차피 끝자리 노드 counter에 의해 queue에서 접근 불가하기에 굳이 Root 노드 값을 다시 저장할 필요없다.
        parent = 1;#루트 노트 index
        leftChild = parent*2;#루트 노드의 왼쪽 자식 index
        rightChild = parent*2 + 1;#루트 노드의 오른쪽 자식 index
        
        while True:#부모와 자식 노드 간 관계를 유지하기 위해 반복되는 내용이다.
            if self.count >= rightChild:#부모 노드가 현재 자식 노드를 둘다 가지고 있는 경우
                if self.queue[parent][1] > self.queue[leftChild][1] or self.queue[parent][1] > self.queue[rightChild][1]:#두 자식 노드 중 하나라도 부모 노드 보다 작은 경우
                    if self.queue[leftChild][1] < self.queue[rightChild][1]:#만약 왼쪽 노드가 더 작다면 이는 부모 노드가 자식 노드 둘다 보다 작은 경우나 왼쪽 노드에만 작은 경우를 커버한다.
                        temp = self.queue[parent];#부모 노드 임시 저장한다.
                        self.queue[parent] = self.queue[leftChild];#부모 노드 위치에 자식 노드를 저장한다.
                        self.queue[leftChild] = temp;#자식 노드 위치에 부모 노드를 넣는다.
                        parent = leftChild;#부모 index를 자리교환된 위치로 업데이트한다.
                    else:#오른쪽 노드가 더 작거나 같다면 이는 부모 노드가 자식 노드 둘다 보다 작은 경우와 오른쪽 노드에만 작은 경우를 의미한다.
                        temp = self.queue[parent];#부모 노드 임시 저장한다.
                        self.queue[parent] = self.queue[rightChild];#부모 노드 위치에 자식 노드를 저장한다.
                        self.queue[rightChild] = temp;#자식 노드 위치에 부모 노드를 넣는다.
                        parent = rightChild;#부모 index를 자리교환된 위치로 업데이트한다.
                else:
                    break;
            elif self.count >= leftChild:#부모 노드가 자식 노드를 하나만 가지고 있는 경우
                if self.queue[parent][1] > self.queue[leftChild][1]:#부모 노드가 자식 노드보다 클 경우 관계 위배, 자리교환 필요하다.
                    temp = self.queue[parent];#부모 노드 임시 저장한다.
                    self.queue[parent] = self.queue[leftChild];#부모 노드 위치에 자식 노드를 저장한다.
                    self.queue[leftChild] = temp;#자식 노드 위치에 부모 노드를 넣는다.
                    parent = leftChild;#부모 index를 자리교환된 위치로 업데이트한다.
                else:#부모 노드와 자식 노드 간 관계가 지켜지기에 바로 while문 빠져 나온다.
                    break;
            else:# 부모 노드가 자식노드 둘다 가지지 않기에 바로 빠져나온다.
                break;
            
            leftChild = parent*2;#업데이트된 부모 노드 index에 맞춰 다음 비교를 위해 왼쪽 자식 노드 index 업데이트
            rightChild = parent*2 + 1;#마찬가지로 오른쪽 자식 노드 index 업데이트

        return ret;#루트 노드에 있던 값을 리턴한다.


        

if __name__ == "__main__":
    pq = PQ();#O(logn)연산으로 최소 edge를 가져오기 위한 Priority Queue이다.
    graph = {};#그래프를 저장하기 위한 Hashmap으로 key: 노드 번호, value: (연결된 노드 번호, 가중치)의 리스트이다.

    n= int(input()); # n은 노드 크기가고 m은 엣지 크기이다.
    m= int(input()); # n은 노드 크기가고 m은 엣지 크기이다.

    
    for j in range(m):#이제 현재 노드와 연결된 정보를 나타내는 엣지들에 대한 정보만들 다룬다.
        node, connectedNode, weight = map(int,input().split(" "));        
        if graph.get(connectedNode) == None:#그래프에 아직 노드 정보가 없을 경우
            graph[connectedNode] = [(node, weight)];#그래프에 노드와 연결된 엣지 정보를 새로 생성해서 넣는다.
        else:#그래프에 연결된 노드에 대한 정보 이미 존재하는 경우
            graph[connectedNode].append((node,weight));#기존 데이터에 현재 엣지에 대한 정보만 추가한다.
        if graph.get(node) == None:#그래프 현재 노드 정보가 없을 경우 위와 같이 생성 or 기존 데이터에 추가한다.
            graph[node] = [(connectedNode,weight)];
        else:#그래프에 연결된 노드에 대한 정보 이미 존재하는 경우
            graph[node].append((connectedNode,weight));#기존 데이터에 현재 엣지에 대한 정보만 추가한다.
    
    mark = [0 for _ in range(n+1)];# 이미 추가된 노드와 추가되기 전 노드에 대한 구분을 위해 mark하기 위한 배열이다.
    minimumSpanningTree = [];# 최종 결과를 저장해 출력하기 위한 변수이다.
    mark[1] = 1;# source 노드에서 시작하기에 바로 mark한다.
    for edge in graph[1]:#source 노드 저장된 엣지들
        pq.insert(edge);#모두 pq에 저장한다.
    
    while(len(minimumSpanningTree) < n-1):#source 노드를 제외 나머지 노드들이 모두 저장(연결)될 때까지 반복된다.
        node, weight = pq.delete();#pq에 저장된 edge 중 가중치가 최소인 것을 가져온다.
        if mark[node] == 0:#만약 가져온 엣지와 연결된 노드가 아직 연결된 노드가 아니라면
            mark[node] = 1;#노드가 이제 연결되었음을 표시한다.
            minimumSpanningTree.append(weight);#그리고 선택된 엣지의 가중치를 결과에 넣는다.

            for edge in graph[node]:#그리고 연결된 노드의 엣지들을
                pq.insert(edge);#모두 pq에 추가한다.
    
    print(minimumSpanningTree);#결과를 출력한다.

# 틀린 사항
# queue에서 부모 노드가 자식이 두개인지 하나인지 구별하지 않음
# 부모 노드와 자식 노드간의 index 계산에 -1이 들어가 0에 -1 계산결과가 나와 의도하지 않은 결과 발생
# 삭제 시 부모와 자식 노드간의 크기 방향 반대로 함
# 노드 삭제 시 제일 마지막 노드와 루트 노드 위치를 바꾼 후 마지막 노드 삭제한 후 마지막 노드가 최소를 유지하는지 확인하는 경우에서
# 노드가 자식 노드를 둘다 갖는지 하나만 갖는지, 자리를 바꿔야 되는지 안 바꿔도 되는지, 바꾼다면 어떠한 것과 바꾸는지 순서로 조건문을 작성 못했다.
# python dict에 저장된 list value를 업데이트하고 싶으면 그냥 [원하는 index].append를 바로 갈기면된다.