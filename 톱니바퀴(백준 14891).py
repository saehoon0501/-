from collections import deque;

gear1 = deque();
gear2 = deque();
gear3 = deque();
gear4 = deque();

for i in range(4):
    n = input();
    if i == 0:
        for j in range(8):
            gear1.append(int(n[j]));
    elif i == 1:
        for j in range(8):
            gear2.append(int(n[j]));
    elif i == 2:
        for j in range(8):
            gear3.append(int(n[j]));
    else:
        for j in range(8):
            gear4.append(int(n[j]));

k = int(input());
turns = [list(map(int, input().split(" "))) for _ in range(k)];

def turnGear(t, turned, gear1, gear2, gear3 ,gear4):    
    number, direction = t;    

    if number == 1 and turned[0] == 0:#기어번호1 선택
        if gear1[2] == gear2[6]:#서로 극 방향이 같아 기어1만 회전
            if direction == 1:#시계 방향인 경우
                turned[0] = 1;
                spinCw(gear1);
            else:
                turned[0] = 1;
                spinCcw(gear1);
        else:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear1);
                turned[0] = 1;
                turnGear((2,-1), turned, gear1, gear2, gear3 ,gear4);
            else:
                spinCcw(gear1);
                turned[0] = 1;
                turnGear((2,1), turned, gear1, gear2, gear3 ,gear4);
    
    elif number == 2 and turned[1] == 0:#기어번호2 선택
        if gear1[2] == gear2[6] and gear2[2] == gear3[6]:#서로 극 방향이 같아 기어1만 회전
            if direction == 1:#시계 방향인 경우
                spinCw(gear2);
                turned[1] = 1;
            else:
                spinCcw(gear2);
                turned[1] = 1;
        elif gear1[2] != gear2[6] and gear2[2] == gear3[6]:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear2);
                turned[1] = 1;
                turnGear((1,-1), turned, gear1, gear2, gear3 ,gear4);
            else:
                spinCcw(gear2);
                turned[1] = 1;
                turnGear((1,1), turned, gear1, gear2, gear3 ,gear4);
        
        elif gear1[2] == gear2[6] and gear2[2] != gear3[6]:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear2);
                turned[1] = 1;
                turnGear((3,-1), turned, gear1, gear2, gear3 ,gear4);
            else:#반시계 방향인 경우
                spinCcw(gear2);
                turned[1] = 1;
                turnGear((3,1), turned, gear1, gear2, gear3 ,gear4);
        else:#맞물린 양쪽 두 기어 모두 선택된 기어와 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우                
                spinCw(gear2);
                turned[1] = 1;
                turnGear((1,-1), turned, gear1, gear2, gear3 ,gear4);
                turnGear((3,-1), turned, gear1, gear2, gear3 ,gear4);
            else:#반시계 방향인 경우                
                spinCcw(gear2);
                turned[1] = 1;
                turnGear((1,1), turned, gear1, gear2, gear3 ,gear4);
                turnGear((3,1), turned, gear1, gear2, gear3 ,gear4);

    elif number == 3 and turned[2] == 0:
        if gear2[2] == gear3[6] and gear3[2] == gear4[6]:#서로 극 방향이 같아 기어1만 회전
            if direction == 1:#시계 방향인 경우
                spinCw(gear3);
                turned[2] = 1;
            else:
                spinCcw(gear3);
                turned[2] = 1;
        elif gear2[2] != gear3[6] and gear3[2] == gear4[6]:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear3);
                turned[2] = 1;
                turnGear((2,-1), turned, gear1, gear2, gear3 ,gear4);
            else:
                spinCcw(gear3);
                turned[2] = 1;
                turnGear((2,1), turned, gear1, gear2, gear3 ,gear4);
        
        elif gear2[2] == gear3[6] and gear3[2] != gear4[6]:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear3);
                turned[2] = 1;
                turnGear((4,-1), turned, gear1, gear2, gear3 ,gear4);
            else:#반시계 방향인 경우
                spinCcw(gear3);
                turned[2] = 1;
                turnGear((4,1), turned, gear1, gear2, gear3 ,gear4);
        else:#맞물린 양쪽 두 기어 모두 선택된 기어와 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우                
                spinCw(gear3);                
                turned[2] = 1;
                turnGear((2,-1), turned, gear1, gear2, gear3 ,gear4);
                turnGear((4,-1), turned, gear1, gear2, gear3 ,gear4);
            else:#반시계 방향인 경우                
                spinCcw(gear3);                
                turned[2] = 1;                
                turnGear((2,1), turned, gear1, gear2, gear3 ,gear4);
                turnGear((4,1), turned, gear1, gear2, gear3 ,gear4);
    elif number == 4 and turned[3] == 0:#기어4번        
        if gear3[2] == gear4[6]:#서로 극 방향이 같아 기어1만 회전
            if direction == 1:#시계 방향인 경우
                spinCw(gear4);
                turned[3] = 1;
            else:
                spinCcw(gear4);
                turned[3] = 1;
        else:#서로 극방향이 다른 경우
            if direction == 1:#시계 방향인 경우
                spinCw(gear4);
                turned[3] = 1;
                turnGear((3,-1), turned, gear1, gear2, gear3 ,gear4);
            else:
                spinCcw(gear4);
                turned[3] = 1;
                turnGear((3,1), turned, gear1, gear2, gear3 ,gear4);
    return;

def spinCcw(gear):
    tmp = gear.popleft();
    gear.append(tmp);

def spinCw(gear):
    tmp = gear.pop();
    gear.appendleft(tmp);    

def score(gear1, gear2, gear3, gear4):
    ret = 0;

    if gear1[0] == 1:
        ret += 1;
    if gear2[0] == 1:
        ret += 2;
    if gear3[0] == 1:
        ret += 4;
    if gear4[0] == 1:
        ret += 8;
    
    return ret;

for t in turns:    
    turned = [0 for _ in range(4)];    
    turnGear(t, turned, gear1, gear2, gear3, gear4);#t는 (기어번호, 회전 방향 1: 시계 -1: 반시계 방향)    
    
ret = score(gear1, gear2, gear3, gear4);
print(ret);