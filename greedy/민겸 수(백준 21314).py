MKs = input().rstrip()

# 최대의 경우 K가 나오전 까지 가장 많은 M을 가지면 된다. 만약 M만 연속된다면 각 M을 따로 나눠 본다.
result = ""
i = 0
Mcount = 0
while True:
    if len(MKs) <= i:
        if Mcount > 0:
            result += "1" * Mcount
        break
    if MKs[i] == "K":
        result += str(10**Mcount * 5)
        Mcount = 0
    else:
        Mcount += 1
    i += 1

print(result)

# 최소의 경우 M와 K를 나눠서 본다.
result = ""
i = 0
Mcount = 0
while True:
    if len(MKs) <= i:
        if Mcount > 0:
            result += str(10 ** (Mcount - 1))
        break
    if MKs[i] == "K":
        if Mcount > 0:
            result += str(10 ** (Mcount - 1))
        result += str(5)
        Mcount = 0
    else:
        Mcount += 1
    i += 1
print(result)
