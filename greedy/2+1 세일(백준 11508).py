N = int(input())
items = []
for _ in range(N):
    cost = int(input())
    items.append(cost)

items.sort(reverse=True)

sum = 0
i = 0
while i < N:
    if i + 2 < N:
        sum += items[i] + items[i + 1]
        i += 3
    else:
        sum += items[i]
        i += 1
print(sum)
