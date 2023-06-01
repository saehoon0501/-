import copy

def move(N, coordinates, target):    
    x,r,c,xi,xj = target
    colCount = moveCol(c-1, xj, N)#행을 회전 시켜야 하는 횟수를 가져온다
    rowCount = moveRow(r-1, xi, N)#열의 회전시킨다.    
    
    count = 0
    for cd in coordinates:
        cx,cr,cc,cxi,cxj = cd
        i,j = cxi, cxj
        #움직인 점과 같은 행에 있다면 같이 움직임 반영
        if cxi == xi:
            j = (cxj+colCount)%N            
        #움직인 점과 같은 열에 있다면 같이 움직임 반영
        if j == (c-1):
            i = (cxi+rowCount)%N
        #그리고 이들을 새로 저장
        coordinates[count] = (cx,cr,cc,i,j)
        count += 1
            
    return colCount + rowCount

def moveCol(t, c, N):
    count = 0
    while c != t:
        c += 1
        c = (c%N)
        count += 1 

    return count

def moveRow(t, c, N):
    count = 0
    while c != t:
        c += 1
        c = (c%N)
        count += 1 

    return count

N,K = map(int, input().split(" "))#표의 크기 N, 숫자의 수 K
coordinates = []#입력된 값들의 위치들을 저장해 추적한다
results = []

for _ in range(K):#숫자 x를 위치 [r-1][c-1]로 이동시켜야 한다.
    x,r,c = map(int, input().split(" "))
    t = (x,r,c)
    coordinates.append((x,r,c,(x-1)//N, (x-1)%N))

while len(coordinates) > 0:
    coord = coordinates.pop(0)
    result = move(N, coordinates, coord)#x를 (r,c) 위치로 이동한다. 그리고 이에 영향 받는 점들도 위치를 반영한다.
    results.append(result)

for result in results:
    print(result)
