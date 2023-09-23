N = int(input())
drinks = list(map(int, input().split()))
drinks.sort(reverse=True)
sum = drinks[0]

for i in range(1, N):
    sum += drinks[i] / 2

print(sum)
