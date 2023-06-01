#상어의 위치에서 방향과 거리(1,2,3,4)에 따라 해당 칸들의 수들을 0(빈칸으로) 만든다.
#이후 토네이도 회전을 돌면서 빈 칸들을 채운다.
#채우는 방식은 만약 0인 칸을 만나면 다음 칸의 값을 가져와 채운 후 그 다음 칸을 0으로 만든다.
#여기서 0칸 다음 칸이 또 0이 나타난다면 해당 칸의 값을 건너 뛰고 다시 숫자가 존재하는 칸이 나올 때까지 찾은 후 그 값을 넣는다.
#그리고 그 가져온 값에 해당하는 칸을 다시 0으로 만든다.
#이렇게 업데이트 후 다시 토네이도에 맞춰 숫자들이 4개 이상 연속하면 폭발하는 것을 넣는다. 이렇게 다 폭발 시키고 나면
#아까 채우는 방식과 같이 똑같이 채운다.
def erase(box, start ,d, s):
    x,y = start;#시작 위치를 저장한다.
    move = 0;

    if d == 1:#위쪽
        move = (-1,0);
    elif d == 2:#아래
        move = (1,0);
    elif d== 3:#왼쪽
        move = (0,-1);
    else:#오른쪽
        move = (0,1);
    
    dx, dy = move;

    for _ in range(s):#해당 거리만큼 방향에 맞게 나아간다.
        if 0<= x+dx < len(box) and 0<= y+dy < len(box):#해당 위치가 인덱스를 벗어나지 않는다면
            box[x+dx][y+dy] = 0;#해당 칸은 빈칸으로 만든다.
        x,y = x+dx, y+dy#그리고 이동한 칸의 방향을 유지하며 다음 칸으로 넘어간다.


def fillHole(box, start):
    moves = [(0,-1), (1,0), (0,1), (-1,0)]#왼 아래 오른쪽 위 순서대로 방향이 바뀐다.
    x,y = start;#시작 위치를 저장한다.
    count = 0;#길이 변화를 언제 주기 확인하기 위해
    length = 0;
    holes = [];
    while x != 0 and y != 0:
        for dx, dy in moves:
            if count % 2 == 0:
                length += 1;
            
            for _ in range(length):
                if 0<= x+dx <len(box) and 0<= y+dy < len(box):
                    if box[x+dx][y+dy] == 0:#만약 빈칸에 도착하면
                        holes.append((x+dx, y+dy))#빈칸 위치를 기억한다.
                    else:#숫자가 존재하는 칸이라면
                        if len(holes) > 0:#그리고 이전에 빈칸이 존재하면
                            holeX, holeY = holes.pop(0);#가장 앞에 있는 빈칸 정보를 가져온다.
                            #그리고 두 칸의 정보를 서로 스위치
                            box[holeX][holeY], box[x+dx][y+dy] = box[x+dx][y+dy], box[holeX][holeY];
                            holes.append((x+dx,y+dy))#그리고 빈칸된 곳 추가시킴                    
                else:#인덱스를 벗어났기에 해당 방향으로 진행 멈춘다.
                    break;
                x,y = x+dx,y+dy#이동 좌표 업데이트
            
            if x == 0 and y == 0:#만약 도착점에 있다면 이제 멈추기에 방향에 따른 loop나와 while문으로 간다.
                break;
            count += 1;#매 방향마다 길이 만큼 이동이 끝나면 카운트 올림

def boom(box, start):
    global boomed;
    moves = [(0,-1), (1,0), (0,1), (-1,0)]#왼 아래 오른쪽 위 순서대로 방향이 바뀐다.
    bomb = [];
    tmp = [];
    x,y = start;#시작 위치를 저장한다.
    count = 0;
    length = 0;
    stop = True;
    while x != 0 and y != 0 and stop:
        for dx, dy in moves:
            if count % 2 == 0:
                length += 1;
            
            for _ in range(length):
                if 0<= x+dx < len(box) and 0<= y+dy < len(box):#인덱스가 존재하면                    
                    if box[x+dx][y+dy] == 0:#빈칸 만나면 이후부터 다 빈칸이라 stop                        
                        stop = False;
                        break;
                    
                    #값이 존재하는 칸의 경우
                    if len(tmp) == 0:#만약 tmp이 비어있다면 일단 추가한다.
                        tmp.append((x+dx,y+dy));#연속된 값 비교를 위해 저장
                    else:#만약 tmp이 채워진 상태라면                        
                        valX, valY = tmp[0];#tmp 값을 가져온다.
                        if box[valX][valY] == box[x+dx][y+dy]:#같은 값이면 추가
                            tmp.append((x+dx,y+dy));
                        else:#아니면 새로 할당 후 가져온 값을 넣는다.
                            if len(tmp) >= 4:#연속된 값이 4개 이상이면 이는 bomb이다.
                                bomb.append(tmp);#bomb에 저장 후                                                        
                            tmp = [(x+dx,y+dy)];#새로 초기화                            
                else:
                    break;
                x,y = x+dx, y+dy
            
            if (x == 0 and y == 0) or not stop:
                if len(tmp) >= 4:#연속된 값이 4개 이상이면 이는 bomb이다.
                    bomb.append(tmp);#bomb에 저장
                break;
            count += 1;
    
    if len(bomb) == 0:
        return True;

    for bs in bomb:        
        if box[bs[0][0]][bs[0][1]] == 1:
            boomed[0] += len(bs);
        elif box[bs[0][0]][bs[0][1]] == 2:
            boomed[1] += len(bs);
        else:
            boomed[2] += len(bs);
    
        for bx,by in bs:
            box[bx][by] = 0;

    return False;

def change(box, start):
    moves = [(0,-1), (1,0), (0,1), (-1,0)]#왼 아래 오른쪽 위 순서대로 방향이 바뀐다.
    tmp = [];
    x,y = start;#시작 위치를 저장한다.
    count = 0;
    length = 0;
    stop = True;
    queue = [];

    while x != 0 and y != 0 and stop:
        for dx, dy in moves:
            if count % 2 == 0:
                length += 1;
            
            for _ in range(length):
                if 0<= x+dx < len(box) and 0<= y+dy < len(box):#인덱스가 존재하면
                    if box[x+dx][y+dy] == 0:#빈칸 만나면 이후부터 다 빈칸이라 stop
                        if len(tmp) == 0:#빈칸을 만났는데 tmp까지 비었다면 종료조건
                            return                        
                        stop = False;
                        break;
                    if len(tmp) == 0:
                        tmp.append((x+dx,y+dy));#연속된 값 비교를 위해 저장           
                    else:#만약 tmp이 채워진 상태라면
                        valX, valY = tmp[0];#tmp 값을 가져온다.
                        if box[valX][valY] == box[x+dx][y+dy]:#같은 값이면 추가
                            tmp.append((x+dx,y+dy));
                        else:#아니면 새로 할당 후 가져온 값을 넣는다.                            
                            queue.append(len(tmp));#queue에 이전 그룹의 개수, 그룹 번호 순으로 저장 후
                            queue.append(box[valX][valY]);
                            tmp = [(x+dx,y+dy)];#새로 초기화
                else:
                    break;
                x,y = x+dx, y+dy
            
            if (x == 0 and y == 0) or not stop:
                valX, valY = tmp[0];
                queue.append(len(tmp));#queue에 이전 그룹의 개수, 그룹 번호 순으로 저장 후
                queue.append(box[valX][valY]);
                break;
            count += 1;

    x,y = start;#시작 위치로 초기화
    count = 0;
    length = 0;
    while x != 0 and y != 0:
        for dx, dy in moves:
            if count % 2 == 0:
                length += 1;
            
            for _ in range(length):
                if 0<= x+dx < len(box) and 0<= y+dy < len(box):#인덱스가 존재하면
                    if len(queue) == 0:
                        box[x+dx][y+dy] = 0;
                    else:
                        amount = queue.pop(0);
                        box[x+dx][y+dy] = amount;
                else:
                    break;
                x,y = x+dx, y+dy
            
            if x == 0 and y == 0:
                break;
            count += 1;        

if __name__=="__main__":
    N,M = map(int, input().split(" "));#N은 칸들의 수와 그 정보, M은 마법의 정보 수를 의미한다.
    box = [list(map(int, input().split(" "))) for _ in range(N)];#N개의 정보를 읽어와 박스를 만든다.
    magic = [tuple(map(int, input().split(" "))) for _ in range(M)];#M개의 마법 정보를 읽어와 저장한다.
    start = (N//2, N//2);
    global boomed;
    boomed = [0]*3;

    for d,s in magic:#마법에 저장된 방향과 거리를 읽는다.
        erase(box, start,d, s);#박스에서 마법에 해당하는 칸들의 숫자들을 없앤다.
        fillHole(box, start);#토네이도에 맞춰 칸들을 채운다.        
        while True:
            if boom(box, start):#채운 칸들에서 폭발이 없을 때까지 폭발과 채우는 과정을 반복한다.
                break;
            fillHole(box, start);
        change(box, start)#폭발이 다 되면 구슬들의 정보에 따라 구슬들을 변화시킨다.

    result = boomed[0]*1 + boomed[1]*2 + boomed[2]*3;
    print(result);
       
