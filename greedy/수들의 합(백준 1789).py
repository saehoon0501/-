a = []

i = 1
sum = 1

while sum <= 4_294_967_295:
    a.append([sum, i])
    i += 1
    sum += i
a.append([sum, i])

s = int(input())

j = 0
while a[j][0] <= s:
    j += 1

print(a[j - 1][1])
