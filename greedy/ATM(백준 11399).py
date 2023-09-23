N = int(input())
line = list(map(int, input().split()))
line.sort()

result = 0
sum = 0
for i in range(N):
    sum += line[i]
    result += sum

print(result)
