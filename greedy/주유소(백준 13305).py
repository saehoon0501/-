N = int(input())
distances = list(map(int, input().split()))
station = list(map(int, input().split()))
cost = 0
i = 0
j = 0

while i < len(station):
    distance = 0

    while j < len(station) and station[i] <= station[j]:
        if 0 < j and i != j:
            distance += distances[j - 1]
        j += 1
    if j < len(station):
        distance += distances[j - 1]
    cost += distance * station[i]
    i = j

print(cost)

# i와 j의 index간 관계를 정확히 이해해서 구현하는게 어려웠음
