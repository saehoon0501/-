import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
sam = list(map(int, sys.stdin.readline().split()))
houses = set()

queue = deque()
for s in sam:
    queue.appendleft([s, 0])
    houses.add(s)


count = 0
sum = 0
while queue:
    i, val = queue.popleft()

    for m in [1, -1]:
        if i + m not in houses:
            count += 1
            sum += val + 1
            houses.add(i + m)
            queue.append([i + m, val + 1])
            if count == K:
                queue = []
                break
print(sum)
