N = int(input())

ropes = [0] * N
for i in range(N):
    ropes[i] = int(input())
ropes.sort()

result = 0
for i in range(N):
    result = max(result, ropes[i] * (N - i))

print(result)
