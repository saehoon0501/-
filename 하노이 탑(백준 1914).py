import sys
sys.setrecursionlimit(10**5)

def hanoi(n, fromPos, toPos, auxPos):    
    if n == 1:        
        print(fromPos, toPos, sep=" ")
        return
    
    hanoi(n-1, fromPos, auxPos, toPos)
    print(fromPos, toPos, sep=" ")
    hanoi(n-1, auxPos, toPos, fromPos)
    return

n = int(input())
print(2**n - 1)
if n <= 20:    
    hanoi(n, 1,3,2)