import sys
def input():
    return sys.stdin.readline().rstrip()

results = [0]*1000
results[0] = 1
results[2] = 1

for i in range(4,1000):
    if results[i-1] * results[i-3] == 1:
        results[i] = 0
    else:
        results[i] = 1

N = int(input())

if results[N-1] == 1:
    print("SK")
else:
    print("CY") 