
def dfs(start, land, tmp, processed, day):
    global L,R;
    moves = [(1,0),(-1,0),(0,1),(0,-1)];

    for dx,dy in moves:
        adjacentLand = (start[0]+dx, start[1]+dy);#인접 국가를 가져온다
        if indexOut(adjacentLand, len(land)):#인접 국가가 land 인덱스를 넘지 않는다면
            if processed[adjacentLand[0]][adjacentLand[1]] == day:#인접 국가가 이미 처리된 국가가 아니라면
                #그리고 시작 국가와 인접 국가 사이에 인구 차가 조건에 만족한다면
                if L <= abs(land[start[0]][start[1]] - land[adjacentLand[0]][adjacentLand[1]]) <= R:
                    tmp.append(adjacentLand);
                    processed[adjacentLand[0]][adjacentLand[1]] += 1;
                    dfs(adjacentLand, land, tmp, processed, day);
    return;

def indexOut(adjacentLand, n):
    if 0<= adjacentLand[0] < n and 0<= adjacentLand[1] < n:
        return True;
    return False;

def populationMerge(united, land):    
    for ns in united:#연합된 국가들 리스트를 가져온다.
        sum = 0;
        for i,j in ns:#그 리스트에서 나라 위치를 하나씩 가져온다.
            sum += land[i][j];#연합 국가들의 총 합을 계산한다.

        population = sum//len(ns);#계산된 총 합에서 국가 수를 나눈다.(소수점은 버린다.)
        
        for i,j in ns:#그 리스트에서 나라 위치를 하나씩 가져온다.
            land[i][j] = population;#연합된 국가들에게 인구이동된 수를 저장시킨다.

if __name__ == "__main__":
    global L, R;
    N, L, R = map(int, input().split(" "));#N은 땅 크기, L<= 인구 차이 <= R일 때 연합 국가됨
    land = [list(map(int, input().split(" "))) for _ in range(N)];#NxN 땅에 대한 인구 수 입력을 받는다.
    processed = [[0]*N for _ in range(N)];#한 턴에 연합처리된 나라를 알기 위해 각 나라마다 턴을 저장한다.
    
    day = 0;
    while True:
        united = [];
        for i in range(N):
            for j in range(N):
                start = (i,j);
                if processed[start[0]][start[1]] != day:#만약 탐색을 시작하는 국가가 한 턴에서 이미 dfs를 통해 연합되었다면 스킵
                    continue;
                tmp = [start];
                processed[start[0]][start[1]] += 1;#먼저 시작 국가의 처리를 표시한다.
                dfs(start, land, tmp, processed, day);#연합 가능한 국가들을 모두 DFS를 통해 찾아낸다.                
                if len(tmp) == 1:
                    continue;                
                united.append(tmp);                
        #인구 이동이 없을 때까지 연합과 인구 이동을 반복 한다. 즉 연합된 국가가 없다면 인구 이동이 멈춘 것이다.
        if len(united) == 0:            
            break;
        #찾은 연합 국가들의 인구 수들을 계산하여 land에 반영한다.
        populationMerge(united, land);        
        day += 1#만약 처리된 국가가 존재한다면 인구 이동 날짜를 올려준다.

    print(day);