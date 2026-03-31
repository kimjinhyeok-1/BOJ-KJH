import sys
input = sys.stdin.readline

n ,m = map(int, input().split())
grid = [[0] * (n+1)]
for _ in range(n):
    grid.append([0] + list(map(int, input().split())))

p = [[0] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1, n+1):
        p[i][j] = p[i-1][j] + p[i][j-1] - p[i-1][j-1] + grid[i][j]

for _ in range(m):
    r1,c1,r2,c2 = map(int, input().split())
    print(p[r2][c2] - p[r2][c1-1] - p[r1-1][c2] + p[r1-1][c1-1])