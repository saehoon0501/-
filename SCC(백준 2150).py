def dfs(marked, src, processed):#dfs를 통해 노드에 post numbering을 한다.
    global graph;#그래프를 저장한다.
    global path;#dfs Tree를 저장한다.
    stack = [];#반복문을 통해 dfs를 하기 위한 stack이다.
    stack.append(src);#시작 노드를 먼저 저장한다.

    while len(stack) > 0:#스택이 빌 때까지 반복한다.
        node = stack.pop();#먼저 스택에서 노드를 가져온다.

        if marked[node] == 0 and processed[node] == 0:#만약 노드가 접근되거나 처리되지 않은 노드라면
            stack.append(node);#해당 노드를 다시 스택에 추가하고
            marked[node] = 1;#노드를 접근되었다고 표시한다.
            for adjacent in graph[node]:#그리고 해당 노드와 인접한 노드들을 가져와
                if marked[adjacent] == 0:#만약 인접한 노드가 접근된적이 없는 노드라면
                    stack.append(adjacent);#이를 스택에 추가시킨다.
        elif processed[node] == 0 and marked[node] == 1:#만약 처리되지 않았지만 접근된 노드라면 이는 dfs 상 아래 노드를 탐색하고 돌아왔다는 뜻이다.
            processed[node] = 1;#그러면 처리를 표시하고
            path.append(node);#post numbering에 순서대로 경로에 추가한다. 여기서 노드는 이제 stack에서 나오게 된다.
        else:#만약 이외 케이스가 존재한다면
            continue;#별 다른 작업을 하지 않는다.
            

def reverseGraph():#그래프의 방향 엣지들을 뒤집어준다.
    global graph;#그래프이다.
    reversed = {i:[] for i in range(1,v+1)};#뒤집어진 그래프를 저장할 변수이다.

    for node in graph.keys():#그래프에 저장된 모든 노드들에 대하여
        for adjacent in graph[node]:#인접 노드가 있다면
            reversed[adjacent].append(node);#뒤집어진 그래프에서 인접 노드에서 현재 노드 방향인 엣지를 추가한다.

    graph = reversed;#위 과정이 끝나면 글로벌 변수 graph에 뒤집어진 그래프를 저장한다.

def findSCC(marked):#SCC를 찾는다 post numbering이 되어있기에 가장 큰 번호를 돌리고 그 다음 가장 큰 번호를 돌리는 방식으로 찾기 가능하다.
    global path;#경로를 가져온다. 이는 post numbering 순서로 노드가 저장되어 있는 상태이다.
    result = [];#결과를 저장할 변수이다.

    for element in path:#post numbering순으로 노드를 꺼내서
        if marked[element] == 0:#만약 노드가 dfs로 접근되지 않은 상태라면
            result.append(dfs2(marked , element));#해당 노드를 시작으로 dfs를 돌리고 그 결과 접근된 번호들을 가진 배열을 저장한다.        
    result.sort();#최종적으로 접근된 번호들을 가진 배열들을 내림차순으로 정렬한다.
    return result;#2d 배열인 결과를 리턴한다.

def dfs2(marked, i):#dfs를 통해 단순 접근만을 한다.
    stack = [];#dfs를 위해 노드를 저장할 스택이다.
    global graph;#그래프이다.
    path = [];#경로이다.
    
    stack.append(i);#먼저 스택에 시작 노드를 저장한다.
    while len(stack) > 0:#스택이 비어있을 때 까지 아래를 반복한다.
        node = stack.pop();#스택에서 노드를 꺼내고
        if marked[node] == 0:#그 노드가 접근되지 않았으면
            path.append(node);#경로에 노드를 추가한다.
            marked[node] = 1;#그리고 노드가 접근된것을 표시한다.
            for adjacent in graph[node]:#그리고 그 노드와 인접한 노드들 모두
                stack.append(adjacent);#스택에 추가한다.    
    path.sort();#최종적으로 접근된 노드들의 번호를 순서에 맞게 저장한다.

    return path;#그리고 접근된 노드들을 리턴한다.

if __name__ == "__main__":
    v, e = map(int, input().split(" "));#v는 노드 수 e는 엣지 수이다.
    global graph;
    global path;
    graph = {i:[] for i in range(1,v+1)};#그래프를 저장할 dict이다. 노드 번호+1 만큼 노드를 저장할 key를 만든다.
    path = [];#경로를 저장할 변수이다.

    for _ in range(e):#엣지들을 입력받고 이를 그래프에 저장한다.
        a, b = map(int, input().split(" "));
        graph[a].append(b);

    marked = [0 for _ in range(v+1)];#노드가 접근되었는지 알기 위해 표시할 배열이다.
    processed = [0 for _ in range(v+1)];#노드가 처리되었는지 알기 위해 표시할 배열이다.
    for i in range(1, len(marked)):#노드들 중 아직 접근되지 않은 노드가 있다면 dfs를 통해 접근해 post numbering을 수행한다.
        if marked[i] == 0:            
            dfs(marked, i, processed); 
    
    reverseGraph();#기존의 그래프를 뒤집는다.    
    path.reverse();#그리고 경로 또한 뒤집는다.post numbering에서 가장 큰 번호의 노드부터 접근해야되기 때문이다. 
    marked = [0 for _ in range(v+1)];#그리고 표시를 위한 배열을 다시 리셋한다.
    results = findSCC(marked);#그리고 scc를 찾는다.

    print(len(results));#최종 결과 scc의 수를 리턴한다.
    for result in results:#그리고 각 SCC마다 구성된 노드 번호를 출력 후 마지막에 -1\n 문자를 출력한다.
        print(*result, end=" -1\n");