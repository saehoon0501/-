import sys# 정수의 최대값을 알기 위한 자료형이다.
sys.setrecursionlimit(10**5);#백준에서 테스트 통과를 위해 recursion 제한 횟수를 늘리기 위한 기본 설정 변경이다.

def merge(array, aux, low, high):#divide되었던 좌표들을 y값을 기준으로 정렬된 상태로 합치기 위한 함수이다.
    for i in range(low, high+1):#먼저 aux배열에다가 array에 값을 그대로 복사해준다.
        aux[i] = array[i];

    median = (low+high)//2;#시작점과 끝점의 중간점을 구한다.
    i, j = low, median+1;#i는 시작점, j는 중간점에 위치한다.

    for k in range(low, high+1):#array에서 k가 시작부터 끝까지 비교를 통해 요소들을 오름차순으로 넣는다.
        if i > median:#만약 i가 median을 초과했다면 이는 이미 왼쪽 요소들이 모두 저장되었다는 뜻이다.
            array[k] = aux[j];#따라서 j가 가리키는 나머지 절반에 해당하는 요소들을 array에 넣어준다.
            j+=1;#이를 위해 매번 할당 후 j 포인터를 앞으로 움직인다.
        elif j > high:#만약 j가 배열 끝을 벗어나면 이는 오른쪽 절반의 요소들을 전부 array에 배치했다는 의미로 나머지 절반을 array에 넣어준다.
            array[k] = aux[i];#따라서 i가 가리키는 나머지 절반에 해당하는 요소들을 array에 넣는다.
            i+=1;#그리고 i를 앞으로 이동시킨다.
        elif aux[i][1] <= aux[j][1]:#만약 i가 가리키는 요소의 y좌표가 j가 가리키는 요소보다 작다면 i가 먼저 array에 들어가야한다.
            array[k] = aux[i];#따라서 i가 가리키는 요소를 array에 할당한다.
            i+=1;#그리고 i를 앞으로 이동시켜 다음 요소를 가리킨다.
        else:#만약 j가 가리키는 요소의 y좌표가 더 작은 경우
            array[k] = aux[j];#j 요소를 array에 넣는다.
            j+=1;#그리고 j를 앞으로 이동시킨다.

    return

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2; #좌표 쌍의 거리 제곱을 구한다.

def getClosestPair(array, aux, low, high):#주어진 좌표들 중 최단거리 쌍을 찾는다.
    if high == low:#만약 배열에 요소가 1개 라면 바로 리턴
        return sys.maxsize;

    if high - low == 1:#만약 배열에 요소가 2개라면         
        distance = dist(array[low], array[high]);
        
        if array[low][1] > array[high][0]:
            array[low], array[high] = array[high], array[low];

        return distance;
    
    median = (low+high)//2;#시작과 끝 사이 중간값을 구한다.
    centerDot = array[median];#좌표 상 x축에서 가운데에 존재하는 점을 가져온다.
    band = min(getClosestPair(array, aux, low, median), getClosestPair(array, aux, median+1, high));#양쪽 절반 중 더 작은 값을 사용해 Band를 만들기 위해 Band width를 저장한다.

    merge(array, aux, low, high)#Band안에 존재하는 좌표를 파악하기 전에 양 쪽에 y로 정렬된 좌표들을 merge하여 전체적으로 y에 따른 오름차순을 만든다.
    dmin = band;#최단거리의 초기값은 Band 폭 값으로 한다.

    for i in range(low, high+1):#좌표 전체를 i를 이용해 훑는다.
        selectedDot = array[i];#먼저 선택된 좌표를 저장해준다.
        if selectedDot[0] < (centerDot[0] + band) and selectedDot[0] > (centerDot[0] - band):#만약 x축에서 가운데 점에서 Band를 만들었을 때 안에 존재하는 점만 최단거리를 계산한다.
            j = i+1;#선택된 점과 비교할 대상은 선택된 점보다 위에 있는 5개의 점이다. 어차피 최단거리를 5개 안에서 나오기에 5개까지만 비교해도 된다.
            count = 0;
            while count < 5 and j < high+1:#비교한 점이 5개가 될 때까지 비교를 진행한다. 만약 5개가 존재하지 않는다면 멈춘다.
                dotInBox = array[j];#먼저 비교할 점을 저장한다.                                
                if dotInBox[0] < (centerDot[0] + band) and dotInBox[0] > (centerDot[0] - band):#비교할 점이 Band 내에 있는지 확인한다. 
                    distance = dist(dotInBox, selectedDot);#있으면 점간의 거리제곱을 구한다.
                    if distance < dmin:#만약 점간의 거리가 현재 최소 거리보다 작거나 같다면
                        dmin = distance;#현재 최소 거리를 업데이트한다.
                    count+=1;#그리고 비교한 점 카운트를 +1 한다.
                j+=1;#비교할 다음 점으로 넘어간다.
    
    return dmin;#양쪽에서 각각 최단거리와 양쪽 간 점들이 서로 짝을 이룰 때 최단거리 비교가 끝났으면 최종 최단거리를 리턴한다.

if __name__ == "__main__":
    n = int(input());#n은 좌표 수 총 개수를 의미한다.
    
    coordinates = [];# 좌표들을 저장할 배열이다.
    aux = [(0,0)]*n;#Divide and Conquer에서 필요한 추가적 배열이다.
    
    for i in range(n):#총 좌표 수 n만큼 좌표를 읽어 드린다.
        x, y = map(int, input().split(" "));#좌표는 x,y로 구성된다.
        coordinates.append((x,y));#tuple(x,y) 상태로 배열에 저장된다.

    coordinates.sort(key=lambda x:x[0]);#x좌표를 이용해 오름차순으로 배열을 정렬한다.
    print(getClosestPair(coordinates, aux, 0, len(coordinates)-1));#최단거리 쌍을 찾는 함수를 콜하고 최단거리를 return 받는다.

    #Divide and Conquer에서 Base 케이스는 2개 1개 경우로 잡자 굳이 3개를 잡기에는 정렬까지 생각했을 때 불필요하게 코드가 길어지기에
    #어떤 값들을 가져와 거기서 최소나 최대를 가져올꺼면 그냥 간단하게 min/max함수를 사용자
    #quick sort에서 밑에서 큰 값을 찾아올라오는 포인터가 배열을 벗어나는 경우도 고려해야한다.
    #python sort에서 Tuple 정렬 시 우선선위 별로(x[1],x[0])등 정렬 가능하다.