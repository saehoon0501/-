N, M, K = map(int, input().split())
castle = list(map(int, input().split()))
rolling = list(map(int, input().split()))

possibleDestory = []
# 돌의 굴러가는 위치에 따라 구간을 나눠 각 합을 구한다.
for i in range(K):
    if i == K - 1:
        possibleDestory.append([sum(castle[rolling[i] - 1 :]), rolling[i] - 1])
    else:
        possibleDestory.append(
            [sum(castle[rolling[i] - 1 : rolling[i + 1] - 1]), rolling[i] - 1]
        )

possibleDestory.sort(key=lambda x: (-x[0]))

results = []

i = 0
while i < M:
    results.append(possibleDestory[i][1])
    i += 1

results.sort()

for r in results:
    print(r + 1)
