import sys
from collections import deque
k = int(input())
w,h = map(int, input().split())

grid  = [list(map(int, input().split())) for _ in range(h)]
dist = [[[-1] * (k+1) for _ in range(w)] for _ in range(h)]

md = [(-1,0),(1,0),(0,-1),(0,1)]
hd = [(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1),(-2,-1),(-2,1)]
if grid[0][0] == 1 or grid[h-1][w-1] == 1: 
    print(-1)
    sys.exit()

q = deque([(0,0,0)])
dist[0][0][0] = 0

while q:
    x,y,z = q.popleft()
    cur = dist[y][x][z]
    if x == w-1 and y == h-1:
        print(dist[y][x][z])
        sys.exit(0)
    for mdx, mdy in md:
        nx1,ny1 = x+mdx,y+mdy
        if not (0<=nx1<w and 0<=ny1<h):
            continue
        if grid[ny1][nx1] == 0 and dist[ny1][nx1][z] == -1:
            dist[ny1][nx1][z] = cur+1
            q.append((nx1,ny1,z))
    if z<k:
        for hdx, hdy in hd:
            nx2,ny2 = x+hdx,y+hdy
            if not (0<=nx2<w and 0<=ny2<h):
                continue
            if grid[ny2][nx2] == 0 and dist[ny2][nx2][z+1] == -1:
                dist[ny2][nx2][z+1] = cur + 1
                q.append((nx2,ny2,z+1))
print(-1)