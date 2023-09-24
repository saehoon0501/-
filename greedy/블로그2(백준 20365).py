N = int(input())
colors = input().rstrip()

rCount = 0
bCount = 0
if colors[0] == "R":
    rCount = 1
else:
    bCount = 1

for i in range(1, len(colors)):
    if colors[i - 1] != colors[i]:
        if colors[i] == "R":
            rCount += 1
        else:
            bCount += 1

print(min(rCount, bCount) + 1)

# 단순히 문자를 count하는 것이 아닌 연속적인 부분을 카운트하는 것이다.
