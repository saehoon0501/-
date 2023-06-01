
n,l = map(int, input().split(" "));
board = [list(map(int, input().split(" "))) for _ in range(n)];

def passage(board, n, l):
    ret = 0;
    #가로 읽기
    for row in board:
        ret += checkRow(row, n, l);

    #세로 읽기    
    for i in range(n):
        tmp = [];
        for j in range(n):
            tmp.append(board[j][i]);
        ret += checkRow(tmp, n, l);

    return ret;

def checkRow(row, n, l):
    before = 0;
    current = 0;
    slope = [];
    
    for i in range(n):
        if i == 0:
            before = row[i];
            continue;
        
        current = row[i];

        if before == current:#값이 서로 같으면 그냥 진행한다.
            before = current;#다음 진행을 위해 이전값에 현재값을 저장한다.
        elif before > current and before == current + 1:#이전값보다 현재값이 더 작은 경우 & 차이가 -1만 나는 경우
            if i+l-1 >= n:#인덱스를 벗어나면 경사로 없다고 판단
                return 0;  
            for j in range(i,i+l):#slope을 위해 l칸 만큼 연속되는 칸 다음에 존재하는지 확인한다.
                if j in slope:#만약 칸이 이미 사용되었으면 중복 경사로이기에 바로 종료
                    return 0;
                slope.append(j);#slope에 사용된것을 알기위해 사용한다.
                if row[j] != current:#만약 경사로에 있는 값이 서로 다른 경우 바로 종료
                    return 0;                                
        elif before < current and current == before + 1:#이전값보다 현재값이 더 큰 경우 & 현재값과 이전값 + 1이 같아야한다.
            if i-l < 0:#인덱스를 벗어나면 경사로 없다고 판단
                return 0;
            for j in range(i-l,i):#slope을 위해 l칸 만큼 연속되는 칸 이전에 존재하는지 확인한다.
                if j in slope:#만약 칸이 이미 사용되었으면 중복 경사로이기에 바로 종료
                    return 0;
                slope.append(j);#slope에 사용된것을 알기위해 사용한다.
                if row[j] != before:#만약 경사로에 있는 값이 서로 다른 경우 바로 종료
                    return 0;                                
        else:
            return 0;
    
        before = current;#다음 진행을 위해 이전값에 현재값을 저장한다.        
    
    return 1;

result = passage(board, n, l);
print(result);