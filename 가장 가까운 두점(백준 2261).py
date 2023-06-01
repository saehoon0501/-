import sys;
import math;

sys.setrecursionlimit(10**5);#재귀 스택 메모리 제한을 바꾸기 위한 설정 변경 코드이다.
input = sys.stdin.readline;#input을 더 빨리 입력 받기 위한 설정이다.
INF = sys.maxsize;#무한대를 나타내기 위해 정수형 최대값을 사용한다.

n = int(input());#n은 점들의 수이다.
dots = [];#입력 받는 점들을 저장하기 위한 리스트이다.

for _ in range(n):#점의 수만큼 좌표를 입력 받고 (x,y) 튜플 형태로 이를 저장한다.
    x, y = map(int, input().split(" "));
    dots.append((x,y));#(x,y)의 정보로 점들을 저장한다.

dots.sort(key=lambda x:(x[0]));

def findClosestPair(dots):#최단거리를 이루는 한 쌍의 점들을 구한다. 분할 및 정복 기법을 사용해 구역을 두개로 나눠서 보고 사이 공간을 본다.
    if len(dots) == 1:#먼저 점이 하나라면 거리가 존재하지 않기에 무한대 값을 리턴한다.
        return INF;
    elif len(dots) == 2:#점이 두개가 존재한다면 두개의 점간의 거리 제곱을 리턴한다.
        dot1 = dots[0];#dot은 (x,y)로 구성되어 있다.
        dot2 = dots[1];
        return (dot1[0]-dot2[0])**2 + (dot1[1]-dot2[1])**2;
    
    median = len(dots)//2;#존재하는 점들 중 가운데 점을 가져온다.
    center = dots[median];#나중에 리스트를 y좌표로 재정렬하여 양 사이드 사이에서의 점간 거리를 구하기 때문에 미리 x좌표 기준 중간점 값을 저장한다.
    band = min(findClosestPair(dots[0:median]), findClosestPair(dots[median:]));#양 사이드 중 더 작은 거리를 band의 폭으로 사용한다.
    
    dots.sort(key=lambda x:(x[1]));#점들을 y값 기준 내림차순으로 새로 정렬한다.

    ret = band;#먼저 리턴할 최단거리는 band의 폭이다.
    for i in range(len(dots)):#중간점 기준 +-band 폭 안에 존재하는 점들 중 자기 자신보다 위에 있는 5개의 점만 보면 최단거리를 구할 수 있다.
        count = 0;
        if dots[i][0] <= int(center[0] + math.sqrt(band)) and dots[i][0] >= center[0] - math.sqrt(band):
            for j in range(i+1,len(dots)):
                if count == 5:
                    break;
                if dots[j][0] <= center[0] + math.sqrt(band) and dots[j][0] >= center[0] - math.sqrt(band):
                    distance = (dots[i][0]-dots[j][0])**2 + (dots[i][1]-dots[j][1])**2;
                    if distance < ret:
                        ret = distance;
                    count += 1;

    return ret;

result = findClosestPair(dots);
print(result);



    
