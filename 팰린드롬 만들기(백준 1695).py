import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
numbers = list(map(int,input().split(" ")))
reverseNums = list(numbers.__reversed__())
dp = [[0]*(N+1) for _ in range((N+1))]

for i in range(1,(N+1)):
    for j in range(1,(N+1)):
        if numbers[i-1] == reverseNums[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(N-dp[N][N])

#문제 조건들을 보고 반례를 생각해보자
#LCS를 응용 또는 투 포인터와 결과를 dp에 저장하는 방법