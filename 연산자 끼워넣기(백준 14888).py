import copy;
from collections import deque;

n = int(input());
numbers = deque(map(int, input().split(" ")));
operators = list(map(int, input().split(" ")));
numbers = deque(numbers);

global maxVal;
global minVal;
maxVal = -1000000000;
minVal = 1000000000;

def dfs(numbers, operators):
    if len(numbers) == 1:        
        global maxVal;
        global minVal;        
        if maxVal < numbers[0]:
            maxVal = numbers[0];
        if minVal > numbers[0]:
            minVal = numbers[0];
    
    for i in range(4):
        if operators[i] == 0:
            continue;
        a = numbers.popleft();
        b = numbers.popleft();
        c = calculate(a,b,i);        
        numbers.appendleft(c);
        operators[i] = operators[i] - 1;        
        dfs(copy.deepcopy(numbers), copy.deepcopy(operators));
        operators[i] = operators[i] + 1;
        numbers.popleft();
        numbers.appendleft(b);
        numbers.appendleft(a);

def calculate(a,b,i):
    if i == 0:#덧셈
        return a+b;
    elif i == 1:#뺄셈
        return a-b;
    elif i == 2:#곱셈
        return a*b;
    else:#나눗셈                
        if a < 0 and b > 0:
            a = - a;
            return -(a//b);                
        else:
            return a//b;

dfs(numbers, operators);
print(maxVal);
print(minVal);