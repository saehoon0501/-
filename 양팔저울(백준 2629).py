def findWeigh(ball, dp):
    if dp[k][ball] == 1:
        return "Y"
    else:
        for i in range(1,len(dp[k])):
            if dp[k][i] == 1:
                if i+ball < len(dp[k]):
                    if dp[k][i+ball] == 1:
                        return "Y"
    
    return "N"

N = int(input())#추 개수
weighs = list(map(int, input().split(" ")))
M = int(input())#구슬 개수
balls = list(map(int, input().split(" ")))

dp = [[0]*(40_001) for _ in range(N)]

for k in range(N):
    w = weighs[k]
    if k == 0:
        dp[k][w] = 1
    else:
        dp[k][w] = 1        
        for i in range(1,len(dp[k])):
            if i+w < len(dp[k]):
                if dp[k-1][i] == 1:
                    dp[k][i+w] = 1            
                    dp[k][i] = 1

results = []
for b in balls:
    results.append(findWeigh(b, dp))

for r in results:
    print(r, end=" ")
print()

#하나의 배열만을 이용해 dp를 하여 업데이트할 경우 업데이트되는 값이 이전 값으로 들어가 반영되면
#업데이트 과정이 꼬이게 됨을 유의한다. 정 안될 경우 2D 배열을 써서 이전 결과와 현재 결과를 분리해서 사용