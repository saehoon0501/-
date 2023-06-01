import copy;

class PQ:#Priority Queue를 Heap 구조로 구현한다.
    def __init__(self):#Priority Queue 생성자이다.
        self.queue = [(0,0) for _ in range(1000)];#PQ에서 데이터를 저장한 배열로 엣지=(노드,가중치)를 저장한다.
        self.count = 0;#PQ에서 저장되는 데이터의 수를 저장한다. 이를 이용해 데이터를 관리한다.
    
    def insert(self, edge):#PQ에서 데이터를 추가할 때 사용한다.
        self.count += 1;#먼저 카운터를 +1로 업데이트 한다.
        self.queue[self.count] = edge;#그 다음 Heap 가장 끝자리에 엣지를 추가한다.
        index = self.count;#추가된 데이터의 index를 저장한다.

        if self.count == 1:#만약 데이터가 하나만 존재한다면 크기를 비교해 부모와 자식 관계를 유지할 필요가 없기에 바로 리턴한다.
            return;
        
        while(self.queue[int(index/2)][1] > self.queue[index][1]):#현재 추가된 노드의 부모와 크기를 비교해 부모의 가중치가 더 작을 때까지 자리교환을 반복한다.
            temp = self.queue[int(index/2)];#부모 노드를 임시 저장한다.
            self.queue[int(index/2)] = self.queue[index];#자식 노드를 부모 노드 자리에 넣는다.
            self.queue[index] = temp;#자식 노드 자리에 부모 노드를 넣는다.
            index = int(index / 2);#자리교환이 된 후 부모 노드로 간 노드의 위치에서 부모 노드와 다시 비교를 위해 index를 업데이트한다.
        
        return;
    
    def delete(self):#PQ에서 가장 최소 가중치 엣지를 하나 pop하기 위한 함수이다.
        ret = self.queue[1];#루트 노드는 항상 가장 최소를 가지기에 이를 리턴하기 위해 임시저장한다.
        self.queue[1] = self.queue[self.count];#그리고 가장 끝에 위치한 노드를 루트 위치에 넣는다.
        self.count -= 1;#기존 루트 노드는 빼왓기에 카운트 -1로 업데이트한다.

        parent = 1;#루트 노드
        leftChild = parent*2;#루트 노드가 가지는 왼쪽 자식 노드 Index
        rightChild = parent*2 + 1;#루트 노드가 가지는 오른쪽 자식 노드 Index
        
        while True:#루트 노드를 pop한 이후 다시 관계를 유지하는 Heap 구조를 유지하기 위해 부모,자식 노드간 비교를 통한 자리교환이다.
            if self.count >= rightChild:#만약 부모 노드가 자식 노드 2개를 가지는 경우
                if self.queue[parent][1] > self.queue[leftChild][1] or self.queue[parent][1] > self.queue[rightChild][1]:#만약 부모 노드가 두 자식 노드 중 하나 보다 더 크다면 관계 위반으로 자리교환 필요하다.
                    if self.queue[leftChild][1] < self.queue[rightChild][1]:#부모 노드가 왼쪽 자식 노드 보다 더 작고 오른쪽 자식 노드는 아닐 경우와 두 자식노드보다 작지만 왼쪽 노드가 더 작은 경우
                        temp = self.queue[parent];#부모노드를 임시저장한다.
                        self.queue[parent] = self.queue[leftChild];#왼쪽 자식 노드를 부모 노드 위치로 이동
                        self.queue[leftChild] = temp;#왼쪽 자식 노드로 부모 노드가 이동
                        parent = leftChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 왼쪽 자식 노드로 업데이트
                    else:#부모 노드가 오른쪽 노드보다 더 작거나 두 자식 노드보다 더 작지만 이 중 오른쪽 자식 노드가 더 작은 경우
                        temp = self.queue[parent];#부모노드를 임시저장한다.
                        self.queue[parent] = self.queue[rightChild];#오른쪽 자식 노드를 부모 노드 위치로 이동
                        self.queue[rightChild] = temp;#오른쪽 자식 노드로 부모 노드가 이동
                        parent = rightChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 오른쪽 자식 노드로 업데이트
                else:#만약 부모 노드가 관계를 유지하는 경우
                    break;#자리교환 불필요하기에 바로 빠져 나온다.
            elif self.count >= leftChild:#만약 부모 노드가 자식 노드를 하나만 가지는 경우 Heap 구조 상 항상 왼쪽 자식 노드만 가진다.
                if self.queue[parent] < self.queue[leftChild]:#부모 노드가 자식 노드보다 더 큰 경우
                    temp = self.queue[parent];#부모노드를 임시저장한다.
                    self.queue[parent] = self.queue[leftChild];#왼쪽 자식 노드를 부모 노드 위치로 이동
                    self.queue[leftChild] = temp;#왼쪽 자식 노드로 부모 노드가 이동
                    parent = leftChild;#이후 이동한 부모 노드가 해당 위치에서 관계를 유지하는지 확인하기 위해 index를 왼쪽 자식 노드로 업데이트
                else:#만약 부모 노드가 관계를 유지하는 경우
                    break;#자리교환 불필요하기에 바로 빠져 나온다.
            else:#만약 부모노드가 자식 노드를 가지지 않은 경우
                break;#비교할 대상이 없기에 바로 빠져 나온다.
            
            leftChild = parent * 2;#부모 노드의 index가 업데이트 됨에 따라 이에 맞춰 왼쪽 노드 index 업데이트
            rightChild = parent * 2 + 1;#부모 노드의 index가 업데이트 됨에 따라 이에 맞춰 오른쪽 노드 index 업데이트
        
        return ret;#루트 노드 값을 리턴한다.(가장 최소 가중치를 가진다.)
    
def dfs(current, parent, mark):#Kruskal에서 연결된 노드간 cycle이 존재하는지 판별하기 위해 dfs를 사용한다.
    ret = False;#cycle이 있는지 없는지 결과를 저장하기 위한 변수로 초기값은 false로 설정한다.
    mark[current] = 1;#현재 dfs를 통해 접근된 노드가 이제 접근되었다는 것을 저장하기 위한 표시 배열이다.
    global graph;#현재 추가된 edge를 통해 나타낸 graph로 dict으로 key는 노드번호 value는 노드가 가지는 엣지=(노드번호,가중치) 리스트다.

    for k in graph[current]:#현재 접근된 노드가 가지는 엣지들을 통해 연결된 노드를 차례로 하나씩 접근한다.
        if mark[k[0]] == 1:#만약 현재 노드와 연결된 노드가 이미 접근되었던 노드라면
            if k[0] != parent:#그리고 그 노드가 바로 이전에서 넘어왔던 부모 노드가 아니라면
                return True;#이는 이미 다른 노드를 차례로 거쳐 해당 노드를 접근했다는 의미이기에 cycle이 생겼다는 뜻이다.
            continue;#만약 부모 노드였다면 단순히 왔던 길을 다시 되돌아갔다는 뜻이기에 cycle이 아니다. continue로 부모 노드로 다시 접근 막는다.
        
        ret = dfs(k[0], current, mark);#현재 노드에서 연결된 노드 중 하나로 이동한다. 그리고 나온 결과를 저장하여 확인해야한다.
        if ret:#만약 다른 노드로 접근하여 path를 쭉 따라가다 cycle이 발견되었다면 True가 리턴되며 dfs 결과 cycle있다는 판정으로 True를 리턴한다.
            return ret;

    return ret;#만약 dfs 결과 cycle이 없다면 False가 리턴된다.

def checkCycleByUnionFind(node, connectedNode, parent):
    rootX = find(node, parent);#루트 노드 찾는다.
    rootY = find(connectedNode, parent);

    if(rootX == rootY):#만약 두 노드의 루트 노드가 같다면 이미 같은 set에 존재한다는 의미이기에 Cycle이 존재 True 리턴
        return True;
    else:#만약 서로 다른 루트 노드를 가진다면 루트 하나를 다른 루트에 향하도록 업데이트한다. 그리고 cycle이 없기에 False 리턴
        parent[rootY] = rootX;#집합을 다른 루트 노드 집합에 Union한다. 성능을 위해 보통 rank까지 따져서 작은 rank Tree를 가지는 집합이 큰 쪽 루트 노드쪽으로 붙는다.
        return False;

def find(node, parent):#노드의 루트 노드를 찾기위한 재귀 함수이다.
    if parent[node] == node:#만약 노드가 자신을 루트 노드로 가진다면 이는 루트 노드라는 의미이기에 노드를 리턴한다.
        return node;
    else:#만약 루트 노드가 아니라 루트 노드 번호를 가지고 있다면
        root = find(parent[node], parent);#루트 노드번호를 index로 루트 노드쪽으로 접근하고 찾으면 루트 노드가 리턴된다.
        parent[node] = root;#그리고 루트 노드를 찾았으니까 루트 노드 값을 노드 index의 배열 위치에 업데이트한다.
    return root;#루트 노드를 리턴한다.
            
if __name__ == "__main__":
    pq = PQ();#엣지들을 저장하여 빠르게 최소값(O(nlogn))을 가져오기 위해 구현한 priority queue를 선언했다.
    global graph;#graph를 전역변수로 선언, 이는 각 함수에서 사용하기 위해 먼저 global 변수이름을 선언 후 다음부터 값을 조작할 수 있다.

    graph = {};#global이 선언되었기에 이제 값을 할당 가능하다.

    n,m = map(int,input().split(" "));#n = 노드 크기 입력받아 저장한다, m = 엣지 크기 입력받아 저장한다.

    for i in range(n):#노드 크기에 맞게 graph에 key로 노드번호를 넣어 초기화를 해준다.
        graph[i+1] = [];#key는 노드번호 value는 빈 리스트로 선언하였다.

    for i in range(m):#엣지 크기만큼 엣지들을 입력 받는다. 
        node, connectedNode, weight = map(int, input().split(" "));# 노드, 연결 노드, 가중치로 구성된다.
        pq.insert((node,weight,connectedNode));#이를 튜플로 묶어 바로 pq에 넣는다.
    
    mark = [0 for _ in range(n+1)];#cycle이 형성되었는지 확인하려면 dfs로 노드에 접근을 할 때 표시를 하는데 이를 각 노드별로 표시하기 위한 배열이다.
    minimumSpanningTree = [];#최소 비용으로 연결된 결과를 저장하기 위한 배열이다.
    parent = [i for i in range(n+1)];#Union find를 통한 Cycle detection을 위해 사용되는 set을 나타내기 위한 배열이다. 배열의 index는 노드번호를 value는 노드의 루트 노드번호를 의미한다.
    
    #DFS를 이용한 cycle detection 부분
    # while len(minimumSpanningTree) < n-1:#항상 최소결과는 노드번호-1의 엣지 수를 가져야 하기에 이를 만족할 때까지만 엣지를 결과에 추가한다.
    #     node, weight, connectedNode = pq.delete();#먼저 pq에 저장된 graph의 전체 엣지들 중 가장 최소값을 가져온다.
    #     graph[node].append((connectedNode,weight));#가장 최소값을 가지는 엣지가 선택되어 그래프에 추가한다.
    #     graph[connectedNode].append((node,weight));#undirected graph이기에 양쪽 노드 모두 엣지에 대한 정보를 추가한다.
    #     hasCycle = dfs(node, 0, copy.deepcopy(mark));#이렇게 graph에 엣지를 추가한 후 cycle이 발생한지 확인한다.
    #     if hasCycle:#만약 사이클이 발생할 경우
    #         graph[node].pop(len(graph[node])-1);#추가했던 엣지를 다시 되돌린다.
    #         graph[connectedNode].pop(len(graph[connectedNode])-1);#양쪽에 추가되었기에 양쪽을 되돌려야 한다.
    #         continue;#그리고 사이클이 발생하였기에 이는 결과에 추가되지 않도록 continue를 한다.
    #     minimumSpanningTree.append(weight);#만약 엣지 추가 결과 cycle이 없다면 이는 결과에 추가한다.
    #     print(minimumSpanningTree);#매번 엣지가 어떻게 추가되는지 파악하기 위해 print 한다.
    
    #Union-Find를 이용한 detection 부분
    # while len(minimumSpanningTree) < n-1:#항상 최소결과는 노드번호-1의 엣지 수를 가져야 하기에 이를 만족할 때까지만 엣지를 결과에 추가한다.
    #     node, weight, connectedNode = pq.delete();#먼저 pq에 저장된 graph의 전체 엣지들 중 가장 최소값을 가져온다.        
    #     hasCycle = checkCycleByUnionFind(node, connectedNode, parent);
    #     if hasCycle:#만약 사이클이 발생할 경우            
    #         continue;#그리고 사이클이 발생하였기에 이는 결과에 추가되지 않도록 continue를 한다.
    #     minimumSpanningTree.append(weight);#만약 엣지 추가 결과 cycle이 없다면 이는 결과에 추가한다.
    #     print(minimumSpanningTree);#매번 엣지가 어떻게 추가되는지 파악하기 위해 print 한다.
            
    print(minimumSpanningTree);#최종 결과를 print한다.
    
# undirected 그래프에서는 self-loop은 불가능하다. 따라서 dfs로 cycle 발생 판별 시 고려 대상 X
# dfs로 cycle 판별 하는 코드 구현 매우 어려웠음.