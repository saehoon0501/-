N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append((int(input())))

coins.sort(reverse=True)

left = K
count = 0
for c in coins:
    if c <= left:
        i = 1
        while c * i <= left:
            i += 1
        count += i - 1
        left -= c * (i - 1)
print(count)
