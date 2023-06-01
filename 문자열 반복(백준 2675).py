import sys;
input = sys.stdin.readline;

t = int(input());#테스트 케이스 수를 의미한다.
temp = [];#입력된 값들을 기억하기 위한 리스트이다.

def repeat(n,s):
    for i in range(len(s)):
        for _ in range(int(n)):
            print(s[i], end="");#각 문자들을 여러번 반복한다.
    print();#문자들이 반복되어 출력되면 마지막에 개행문자를 넣어 줄 바꿈 처리한다.

for _ in range(t):
    n, s = map(str,input().split(" "));
    temp.append((n,s));

for n,s in temp:
    s = s[0:len(s)-1];#escape 문자를 빼주고 문자를 넘겨준다.
    repeat(n,s);#n은 반복 횟수, s는 총 문자열이다. 문자열의 각 문자를 n번 반복해 출력한다.


