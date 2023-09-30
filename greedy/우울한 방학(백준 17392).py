N, M = map(int, input().split())
plans = list(map(int, input().split()))

cover = 0
for p in plans:
    cover += p + 1

count = M - cover
val = 0
result = 0
if count > 0:
    while True:
        val += 1
        for i in range(N + 1):
            result += val**2
            count -= 1
            if count == 0:
                break
        if count == 0:
            break

print(result)
