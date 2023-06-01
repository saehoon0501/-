tiles = [0]*1000

tiles[0] = 1
tiles[1] = 3

for i in range(2,1000):
    tiles[i] = tiles[i-1] + 2*tiles[i-2]

N = int(input())
print(tiles[N-1]%10_007)