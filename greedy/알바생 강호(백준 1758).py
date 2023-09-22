N = int(input())
tips = []

for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

result = 0
for i in range(N):
    tip = tips[i] - (i)
    if tip <= 0:
        continue
    else:
        result += tip
print(result)
