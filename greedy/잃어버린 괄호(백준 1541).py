expressions = input().rstrip().split("-")
i = 0
number = ""
results = []

for e in expressions[1:]:
    result = 0
    sums = e.split("+")
    for i in range(len(sums)):
        result += int(sums[i])
    results.append(result)

result = 0
for e in expressions[0].split("+"):
    result += int(e)

for r in results:
    result -= r

print(result)
