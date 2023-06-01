
def tornado(box, center):
    moves = [(0,-1),(1,0),(0,1),(-1,0)];
    count = 0;
    length = 1;
    x,y = center;
    sandOutOfBox = 0;

    while True:#(0,0)으로 갈 때까지 반복한다.        
        for dx, dy in moves:
            
            if count != 0 and count % 2 == 0:#카운트가 2배수가 될 때마다 이동거리가 2배씩 증가한다.
                length += 1;            
            for _ in range(length):#이동거리 만큼 해당 방향으로 이동한다.                
                x, y = x+dx, y+dy;
                
                if 0 > x or x >= len(box) or 0 > y or y >= len(box[x]):                    
                    x -= dx;
                    y -= dy;
                    break;
                sandOutOfBox += blowSand((x,y), (dx,dy), box);                
            
                if x == 0 and y == 0:#만약 이동한 칸이 (0,0)이면 종료조건
                    break;
            if x == 0 and y == 0:
                break;            
            count += 1;        
        if x == 0 and y == 0:
            break;
    return sandOutOfBox;

def blowSand(pos, move, box):
    x, y = pos;
    sand = box[x][y];    
    sum = 0;
    sandOutOfBox = 0;

    if move == (0,-1):#왼쪽으로 이동 시
        scatter = [(-2,0,0.02), (-1,-1,0.1), (-1, 0,0.07), (-1,1,0.01), (0,-2,0.05),
                   (1,-1,0.1),(1,0,0.07), (1,1,0.01), (2,0,0.02)];
        for dx, dy, p in scatter:
            if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):#모래가 이동되는 칸이 존재하면 해당 칸에 넣는다.
                box[x+dx][y+dy] += int(sand*p);
                sum += int(sand*p)
                continue;
            sandOutOfBox += int(sand*p);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
            sum += int(sand*p);
        
        dx, dy = 0, -1;
        if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):                                
            box[x+dx][y+dy] += box[x][y] - int(sum);
        else:
            sandOutOfBox += box[x][y] - int(sum);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
        box[x][y] = 0;
    elif move == (1,0):#아래로 이동 시
        scatter = [(0,-2,0.02), (-1,-1,0.01), (0, -1,0.07), (1,-1,0.1), (2,0,0.05),
                   (-1,1,0.01),(0,1,0.07), (1,1,0.1), (0, 2,0.02)];
        for dx, dy, p in scatter:
            if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):
                box[x+dx][y+dy] += int(sand*p);
                sum += int(sand*p);
                continue;
            sandOutOfBox += int(sand*p);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
            sum += int(sand*p);        

        dx, dy = 1, 0;
        if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):
            box[x+dx][y+dy] += box[x][y] - int(sum);            
        else:
            sandOutOfBox += box[x][y] - int(sum);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
        box[x][y] = 0;
    elif move == (0,1):#오른쪽으로 이동 시
        scatter = [(-2,0,0.02), (-1,-1,0.01), (-1, 0,0.07), (-1,1,0.1), (0,2,0.05),
                   (1,-1,0.01),(1,0,0.07), (1,1,0.1), (2,0,0.02)];
        for dx, dy, p in scatter:
            if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):
                box[x+dx][y+dy] += int(sand*p);
                sum += int(sand*p);
                continue;
            sandOutOfBox += int(sand*p);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
            sum += int(sand*p);        

        dx, dy = 0, 1;
        if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):                                
            box[x+dx][y+dy] += box[x][y] - int(sum);
        else:
            sandOutOfBox += box[x][y] - int(sum);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
        box[x][y] = 0;
    else:#위로 이동 시
        scatter = [(0,-2,0.02), (-1,-1,0.1), (0, -1,0.07), (1,-1,0.01), (-2,0,0.05),
                   (-1,1,0.1),(0,1,0.07), (1,1,0.01), (0, 2,0.02)];
        for dx, dy, p in scatter:
            if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):
                box[x+dx][y+dy] += int(sand*p);
                sum += int(sand*p);
                continue;
            sandOutOfBox += int(sand*p);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
            sum += int(sand*p);
        
        dx, dy = -1, 0;
        if 0 <= x+dx < len(box) and 0 <= y+dy < len(box[x]):                                
            box[x+dx][y+dy] += box[x][y] - int(sum);
        else:
            sandOutOfBox += box[x][y] - int(sum);#아니면 밖으로 나간 모래를 구하는 곳에 더한다.
        box[x][y] = 0;
    
    return sandOutOfBox;

if __name__=="__main__":
    N = int(input());#격자 크기
    box = [list(map(int, input().split(" "))) for _ in range(N)];
    center = (N//2, N//2);    

    result = tornado(box, center);
    print(result);