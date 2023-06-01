
class stack:
    def __init__(self):
        self.stack = [0 for _ in range(10000)];
        self.size = 0;

    def push(self, x):
        self.stack[self.size] = x;
        self.size += 1;        

    def pop(self):
        if self.empty() == 1:
            return -1;    
        ret = self.stack[self.size-1];
        self.size -= 1;
        
        return ret;
    
    def empty(self):        
        if self.size == 0:
            return 1
        return 0;

    def top(self):        
        if self.empty() == 1:
            return -1;
        return self.stack[self.size-1];

    def sizeStack(self):        
        return self.size;

n = int(input());
cmd = [list(map(str, input().split(" "))) for _ in range(n)];
s = stack();

for c in cmd:    
    if c[0] == "push":#스택에 정수를 넣는다.
        s.push(int(c[1]));
    elif c[0] == "pop":#스택에 정수를 빼고 출력
        print(s.pop());
    elif c[0] == "size":#스택에 정수의 개수를 출력
        print(s.sizeStack());
    elif c[0] == "empty":#스택이 비어있으면 1 아니면 0 출력
        print(s.empty());
    else:#top, 스택의 가장 위에 있는 경수 출력
        print(s.top());
