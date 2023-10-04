import sys

input = sys.stdin.readline

S = 0

for _ in range(int(input())):
    cmd = input().strip().split()

    if cmd[0] == "all":
        S = (1 << 21) - 1

    elif cmd[0] == "empty":
        S = 0

    elif cmd[0] == "add":
        S |= 1 << int(cmd[1])

    elif cmd[0] == "remove":
        S &= ~(1 << int(cmd[1]))

    elif cmd[0] == "check":
        print(1 if S & (1 << int(cmd[1])) != 0 else 0)

    elif cmd[0] == "toggle":
        S ^= 1 << int(cmd[1])
