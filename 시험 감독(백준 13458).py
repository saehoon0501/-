
n = int(input());#시험장의 개수
a = input().split(" ");#각 시험장의 응시자 수
b,c = map(int, input().split(" "));#총 감독관이 감시 가능한 응시자 수 b, 부감독관은 c
minimumNum = 0;#최소 감독관 수를 저장한다.

for room in a:#각 시험장 마다 필요한 감독관 수들을 구하고 이를 합한다.
    rest = int(room) - b;#먼저 총 감독관은 항상 1명이 있어야하기에 먼저 뺀다.
    minimumNum += 1;
    
    if rest > 0:#그리고 총 감독관이 커버하지 못하는 경우 부감독관들을 계산한다.
        minimumNum += rest//c;

        if rest % c == 0:
            continue;
        minimumNum += 1;        
        
print(minimumNum);