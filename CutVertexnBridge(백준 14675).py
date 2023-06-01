import sys;
sys.setrecursionlimit(10**5);

def dfs(results, nodeNum, count, n):#dfs를 통해 dfsTree를 만들고 edge와 vertex가 ap인지 판단한다.
    global graph#그래프 전역변수를 가져온다.
    children = 0;#루트 노드는 별도로 자식 노드 수를 사용해 판단하기에 이를 위해 자식 수를 카운트한다.
    nodeNum[n] = count;#노드 번호는 접근된 순서에 따라 할당된다.
    ret = nodeNum[n];#초기 리턴 값은 자기 자신의 노드 번호이다.

    for edge in graph[n]:#노드 n과 adjacent 노드들을 살펴본다.
        if nodeNum[edge] == 0:#만약 아직 접근되지 않은 노드라면
            children += 1;#자식 노드임으로 +1한다.
            subTree = dfs(results, nodeNum, count+1, edge);#그리고 해당 노드가 Reachable한 최대 노드 번호를 가져온다.
            if count != 1 and subTree >= nodeNum[n]:#만약 노드 n 아래 subTree에서 노드 n을 넘어 Reach하지 못한다면
                results[n] = True;#노드 n은 ap이다.
            ret = min(ret, subTree);#subTree에서 더 높은 노드로 갈 수 있다면 그 노드 번호를 업데이트 한다.
        else:#만약 이미 접근된 노드라면 부모 노드 또는 Back Edge이다.
            ret = min(ret, nodeNum[edge]);#그리고 그 접근된 노드번호가 더 높은 노드라면 업데이트한다.
    
    if count == 1 and children >=2:#루트 노드가 자식 노드를 2개 이상 가진다면
        results[n] = True;#루트 노드는 ap이다.
    
    return ret;#노드 n에서 Reach 가능한 가장 높은 노드 번호를 리턴한다.

n = int(input());#노드 수를 나타내는 n이다.
global graph#그래프를 나타내기 위한 변수이다.
graph = {i:[] for i in range(1,2*n)};#노드 수는 cut edge도 판별하기 위해서 노드 수 + Edge 수 만큼 할당한다.

for i in range(n-1):#노드 수 -1만큼 Edge를 입력받는다.
    x,y = map(int, input().split(" "));#노드x와 y를 연결하는 edge를 입력받는다.
    graph[x].append(n+i+1);#edge가 cut edge인지 판별하기 위해서는 edge에 추가로 노드를 넣고 ap인지 판단하면 된다.
    graph[y].append(n+i+1);#x,y 사이에 한 노드를 추가하여 할당한다.
    graph[n+i+1].append(x);#그리고 추가한 노드와 x,y를 연결한다.
    graph[n+i+1].append(y);

results = [False]*(2*n);#cut Vertex 또는 Edge인지 판단한 결과를 가진다.
nodeNum = [0]*(2*n);#노드 접근에 따라 매긴 번호를 저장하는 array이다.
dfs(results, nodeNum, 1, 1);#dfs를 통해 Graph에서 Tree를 만들며 cut Vertex 또는 Edge를 판단한다.

k = int(input());#Edge 또는 Vertex가 ap인지 질문하는 수이다.
questions = [];#질문을 저장하기 위한 배열이다.
for _ in range(k):#질문 수 만큼 질문을 받는다.
    type, num = map(int, input().split(" "));#질문 type이 1이면 노드, 2이면 edge에 대한 질문이다.
    questions.append((type, num));#질문들을 저장한다.

for type, num in questions:#질문들을 가져온다.
    if type == 1:#만약 노드가 ap인지에 대한 질문이라면,
        if results[num] == True:#만약 노드가 ap가 맞다면
            print("yes");#yes를 출력
        else:#아니라면
            print("no");#no를 출력한다.
    else:#Edge에 대한 질문인 경우
        if results[n+num] == True:#Edge에 추가한 노드가 ap라면
            print("yes");#Edge도 ap이기에 yes를 출력한다.
        else:#아닌 경우
            print("no");#no를 출력한다.