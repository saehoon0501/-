N = int(input())

f = N // 5
result = -1
while f >= 0:
    if N - (f * 5) == 0:
        result = f
        break
    elif (N - f * 5) % 3 == 0:
        result = f + (N - f * 5) // 3
        break
    else:
        f -= 1

print(result)
