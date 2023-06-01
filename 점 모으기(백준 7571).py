n,m = map(int, input().split(" "));

sumX = 0;
sumY = 0;

dots = [];

minDistanceX = 1;
minDistanceY = 1;

for _ in range(m):
    x, y = map(int, input().split(" "));
    dots.append((x,y));

dots.sort(key = lambda x: x[0]);
medianX = dots[len(dots)//2][0];

dots.sort(key= lambda x:x[1]);
medianY = dots[len(dots)//2][1];

result = 0;
for dot in (dots):
    result += abs(medianX - dot[0]);
    result += abs(medianY - dot[1]);

print(result);

