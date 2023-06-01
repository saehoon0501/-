import sys;

def countTri(graph, edge):#그래프에 존재하는 삼각형 갯수 세는 함수이다.
    answer = 0;#총 삼각형 수를 저장하기 위한 변수

    for e in edge:#엣지들 마다 반복한다.
        x = e[0];#엣지에서 노드 x 번호
        y = e[1];#엣지에서 노드 y 번호

        for node in graph:# 그래프에서 각 노드마다 연결 상태를 가져온다.
            if node[x-1] == 1 and node[y-1] == 1:#만약 해당 노드가 x,y 모두 연결되어있다면
                answer += 1;#모두 연결된 삼각형일 것이기에 카운트 +1을 해준다.
    
    return answer / 3;# 점과 변을 셀 경우 총 3번의 중복된 카운트가 되기에 이를 3으로 나눠야 한다.


if __name__ == "__main__":
    N, M = map(int, input().split(" ")); # N: 바나나 개수, M: 엣지 개수
    graph = [[0]*N for _ in range(N)]; #인접 그래프 행렬
    edge = [];# 엣지들을 저장할 2중 배열

    for i in range(M):#엣지 수 만큼 반복한다.
        x, y = map(int, input().split(" "));#엣지들은 연결된 x 노드와 y 노드로 구성된다.
        edge.append([x,y]);#엣지 배열에 [노드x,노드y]에 대한 연결 정보를 저장한다.
        graph[x-1][y-1] = 1;# 노드x와 연결된 노드 관계를 나타내기 위해 인접배열에 1로 표시
        graph[y-1][x-1] = 1;# 노드y와 연결된 노드 관계를 나타내기 위해 인접배열에 1로 표시

    print(int(countTri(graph, edge)));
    print(sys.getsizeof(graph))