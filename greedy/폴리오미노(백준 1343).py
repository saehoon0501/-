A = input()

A = A.replace("XXXX", "AAAA")
A = A.replace("XX", "BB")

if "X" in A:
    print("-1")

else:
    print(A)
