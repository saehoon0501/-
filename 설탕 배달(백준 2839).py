bags = [-1]*5000
bags[2] = 1
bags[4] = 1

for i in range(5,5000):    
    if bags[i-3] == -1:
        if bags[i-5] == -1:
            continue
        else:
            bags[i] = bags[i-5] + 1
    else:
        if bags[i-5] == -1:
            bags[i] = bags[i-3] + 1
        else:
            bags[i] = min(bags[i-3]+1, bags[i-5]+1)

N = int(input())
print(bags[N-1])
