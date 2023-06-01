stepSize = int(input())
stairs = [0]*(stepSize+1)

for i in range(1,stepSize+1):
    SCORE = int(input())
    stairs[i] = SCORE

sums = [0]*(stepSize+1)
sums[1] = stairs[1]
if stepSize == 1:
    print(sums[1])    
elif stepSize == 2:    
    sums[2] = sums[1] + stairs[2]
    print(sums[2])
else:
    sums[2] = sums[1] + stairs[2]
    for i in range(3,stepSize+1):
        sums[i] = max(sums[i-2]+stairs[i],sums[i-3]+stairs[i-1]+stairs[i])
    print(sums[stepSize])