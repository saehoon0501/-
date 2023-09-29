from fractions import Fraction

p, q, a, n = map(int, input().split())

answer = Fraction(p, q)
global result
result = 0


def dfs(sum, start, multiple, count):
    global result
    if multiple > a:
        return
    if count <= n and sum == answer:
        result += 1
        return

    for i in range(start, (a // multiple) + 1):
        if sum + Fraction(1, i) <= answer:
            dfs(sum + Fraction(1, i), i, multiple * i, count + 1)
    return


dfs(0, 1, 1, 0)
print(result)
