import sys
from collections import deque
input = sys.stdin.readline

m,n,h = map(int, input().split())
d = [(1,0,0),(-1,0,0),(0,-1,0),(0,1,0),(0,0,1),(0,0,-1)]

grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(n):
    for j in range(m):
        for k in range(h):
            if grid[k][i][j] == 1:
                q.append((i,j,k))
                dist[k][i][j] = 0

while q:
    r,c,f = q.popleft()
    for dr, dc, df in d:
        nr,nc,nf = r+dr, c+dc, f+df
        if 0<= nr < n and 0<= nc < m and 0<= nf < h:
            if grid[nf][nr][nc] == 0 and dist[nf][nr][nc] == -1:
                grid[nf][nr][nc] = 1
                dist[nf][nr][nc] = dist[f][r][c] + 1
                q.append((nr,nc,nf))

ans = 0
for i in range(n):
    for j in range(m):
        for k in range(h):
            if grid[k][i][j] == 0:
                print(-1)
                sys.exit(0)
            else:
                ans = max(ans, dist[k][i][j])

print(ans)