import sys

MAXINT = sys.maxsize
T = int(input())
matches = [0, 0, 1, 7, 4, 2, 0, 8]
maxDp = [""] * 101
minDp = [0, 9, 1, 7, 4, 2, 6, 8] + [MAXINT] * 94

maxDp[2] = "1"
maxDp[3] = "7"

for i in range(4, 101):
    maxDp[i] = maxDp[i - 2] + "1"

    if i > 7:
        for j in range(2, 8):
            minDp[i] = min(minDp[i - j] * 10 + matches[j], minDp[i])

for _ in range(T):
    tmp = int(input())
    print(minDp[tmp], maxDp[tmp])
