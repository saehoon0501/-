import math;

def isCw(first, second, third):#CW 방향인지 판별한 결과를 알려준다.
    existedLine = ((second[0]-first[0]),(second[1] - first[1]));#추가되기 전 턴에 이은 선분이다.
    addedLine = ((third[0]-first[0]),(third[1] - first[1]));#이번 턴에 이은 선분이다.

    if existedLine[0]*addedLine[1] - addedLine[0]*existedLine[1] < 0:#만약 CW방향이면 거짓을 Return한다. 일직선 상인 경우는 해당하지 않는다.
        return False;
    
    return True;

def sortByDegree(dots):#각도를 이용한 정렬이다.
    degrees = [];
    start = dots[0]#시작점은 좌표 중 가장 왼쪽 상단에 위치한 점이다.
    for i in range(1,len(dots)):#시작점에서 모든 점들와 각각 이루는 각도를 살펴본다.
        dx, dy = dots[i][0]-start[0], dots[i][1]-start[1];#먼저 두 좌표의 x,y의 차이를 구한다.
        degree = math.atan2(dy, dx);#이를 이용해 arc tangent로 각도를 구한다. 시작점을 x축 기준으로 CCW면 + 각도, CW면 - 각도가 나온다.
        degrees.append((dots[i][0],dots[i][1],degree));#이러한 각도의 결과들을 새로 저장한다.
    
    degrees.sort(key=lambda x:(-x[2],x[1],x[0]));#우선순위에 맞게 정렬되며 1.각도가 클 수록 2.y가 작을 수록 3.x가 작을 수록 앞에 위치한다.
    degrees.insert(0, (start[0],start[1],0));#시작점을 정렬된 배열 맨 앞에 넣어주면 정렬이 끝난다.

    return degrees;

def findConvex(dots):#0을 시작점으로 1을 이은 후 비교점이 CW방향인지 확인하여 맞으면 이어주고 아니면 stack에서 pop한 후 비교점을 추가한다.
    stack = [];
    stack.append(dots[0]);#항상 시작점은 0으로 좌표상 가장 왼쪽에 존재한다.
    stack.append(dots[1]);#시작점에서 가장 큰 각도를 이루는 점을 잇고 시작한다.

    for i in range(2, len(dots)):#이후 점들을 돌아가며 Convex에 적합한지 본다.
        stack.append(dots[i]);#일단 선분을 이어본다.
        lastest = len(stack)-1;#그리고 stack의 변경된 사이즈를 가져온다.
        while isCw(stack[lastest-2], stack[lastest-1],stack[lastest]) and lastest > 1:#추가된 점과 이전 선분이 이루는 방향이 CW일 때까지 한다.
            stack.pop();#만약 CCW 또는 일직선 상이라면 이전에 추가되었던 점이 잘못 되었다는 뜻이기에 이를 제거한다.
            stack.pop();
            stack.append(dots[i]);#그리고 이번 턴에 추가되는 점을 다시 추가한다.
            lastest = len(stack)-1;#stack 사이즈에 맞게 업데이트한다.
    
    if isCw(stack[len(stack)-2],stack[len(stack)-1], stack[0]):#마지막점이 추가될 때 이는 시작점과 연결되기에 시작점과 이루는 방향을 확인한다.
        stack.pop();#만약 CCW방향 또는 일직선 상이라면 그 점은 필요 없는 점이기에 제거한다.
        return stack;#최종 Convex점을 가진 Stack을 리턴한다.
    
    return stack;

n = int(input()) #총 점들의 개수
dots = [];

for i in range(n):#모든 점들의 정보를 dots 변수에 저장한다.
    dots.append(tuple(map(int, input().split(" "))));

dots.sort(key=lambda x:(x[0],-x[1]));#x좌표가 작을 수록 그 다음 그 중 y좌표가 클 수록 배열의 앞에 위차하게 배치한다.
dots = sortByDegree(dots);#좌표중 가장 왼쪽 위에 있는 좌표에 x축을 그어 거기에 arc tangent로 반시계방향이면 +, 시계방향은 -를 부호로 각도를 계산해 내림차순으로 계산한다.
result = findConvex(dots);#각도로 정렬된 좌표에서 Convex를 찾는다. O(n) 걸린다.
print(len(result));