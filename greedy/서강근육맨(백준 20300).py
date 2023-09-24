N = int(input())
training = list(map(int, input().split()))
training.sort()
M = 0
if N % 2 == 0:
    i = 0
    j = N - 1
    while i < j:
        M = max(M, training[i] + training[j])
        i += 1
        j -= 1
    print(M)
else:
    i = 0
    j = N - 2
    while i < j:
        M = max(M, training[i] + training[j])
        i += 1
        j -= 1
    M = max(M, training[N - 1])
    print(M)
