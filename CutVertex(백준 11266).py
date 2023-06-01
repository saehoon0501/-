import sys;
sys.setrecursionlimit(10**5);
INF = sys.maxsize;

def dfs(nodeNum, results, n, count):#dfs를 통해 Articulation Point인지 확인하는 함수이다.
    nodeNum[n] = count;#count된 수에 따라 노드 level이 할당된다.
    global graph;#전역변수 graph를 사용한다.
    ret = nodeNum[n];#리턴 값은 먼저 자기 자신 노드의 level에 따라 부여된 번호를 저장한다.
    children = 0;#루트 노드는 따로 자식 노드를 2개이상 가지는지 판단을 통해 ap인지 확인해야하기에 이를 위한 자식 수를 저장할 변수이다.

    for edge in graph[n]:#노드 n에 있는 edge와 연결된 adjacent 노드들을 dfs한다.
        if nodeNum[edge] == 0:#만약 adjacent 노드의 번호가 없다면 이는 아직 접근되지 않았다는 뜻이다.
            children +=1 ;#노드 n에서 시작하는 dfs Tree의 자식이 하나 추가되고
            subTree = dfs(nodeNum, results, edge, count+1);#그 자식 노드에 대한 dfs로 이동한다. dfs가 끝나면 자식 노드가 접근가능한 최대 높이를 리턴한다.
            if count != 1 and subTree >= nodeNum[n]:#만약 count가 1이 아니라면 자식 노드이기에 해당 노드가 ap인지 판단하기위해 노드 번호와 자식 노드가 최대로 접근 가능한 노드를 비교한다.
                results[n] = True;#만약 자식노드가 최대로 접근 가능한 노드가 자기 자신보다 더 위에 있다면 노드 n은 ap가 된다.
            ret = min(ret, subTree);#노드 n에서 접근 가능한 노드가 자식 노드에서 접근 가능한 노드 중 더 높은 노드 값을 리턴값에 저장한다. 자기 자신이 제일 높은 노드가 아니라면 자식 노드를 거쳐서 더 높은 노드로 갈 수 있기 때문이다.
        else:#만약 자식 노드가 이미 접근된 상태라면 이는 부모 노드 또는 back edge로 연결된 노드일 것이다.
            ret = min(ret, nodeNum[edge]);#만약 접근한 노드가 더 높은 노드로 Reachable한 노드라면 그걸로 값을 업데이트한다.
        
    if count == 1 and children >=2:#count가 1이라면 루트 노드이기에 자식을 2개 이상 가지면 이는 ap이다.
        results[n] = True;#따라서 루트 노드에 대해 True값을 할당한다.
    
    return ret;#리턴값은 결국 노드 n이 Reachable한 노드들 중 dfs Tree상 가장 높은 노드를 가지고 리턴하게 된다.

if __name__=="__main__":
    n,m = map(int, input().split(" "));#n: 노드 수, m: 엣지 수
    global graph;#그래프를 저장하는 전역 변수 
    graph = {i:[] for i in range(1,n+1)};#주어지는 그래프 노드 수에 맞춰 edge들을 저장하기 위해 initialize한다.

    for _ in range(m):#edge 수들 만큼 정보를 입력 받는다.
        x, y = map(int, input().split(" "));#노드 x와 y 사이에 edge를 입력 받는다.
        graph[x].append(y);#노드 x에 y에 대한 edge 추가
        graph[y].append(x);#노드 y에 x에 대한 edge 추가

    nodeNum = [0]*(n+1);#dfs로 Tree가 만들어질 때 Tree height에 따른 번호를 노드마다 저장할 array이다.
    results = [False]*(n+1);#해당 노드가 Atriculation Point(단절점)인지 판단 결과를 저장할 array이다.

    for i in range(1,n+1):#여러 Connected Component가 존재하기에 이를 위해 모든 노드들을 한번씩 꺼낸다.
        if nodeNum[i] == 0:#만약 아직 dfs가 수행되지 않은 노드라면 Reachablity에 따라 새로운 Connected Component가 있음을 의미한다.
            count = 1;#새로운 dfsTree마다 처음 루트는 높이가 1이기에 count를 1로 한다.
            dfs(nodeNum, results, i, count);#루트 노드를 시작으로 Reachable한 모든 노드를 dfs로 찾아낸다.

    answer = [i for i, result in enumerate(results) if i > 0 and result];
    print(len(answer));
    print(*answer);