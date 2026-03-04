import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
dist = [[[-1] * 2 for _ in range(m)] for _ in range(n)]

q = deque([(0,0,0)])

d = [(0,1),(0,-1),(1,0),(-1,0)]

dist[0][0][0] = 1

while q:
    r, c, des = q.popleft()
    if r == n-1 and c == m-1:
        print(dist[n-1][m-1][des])
        exit(0)
    for dr, dc in d:
        nr = r + dr
        nc = c + dc
        if 0<= nr < n and 0<= nc < m:
            if a[nr][nc] == 0 and dist[nr][nc][des] == -1:
                dist[nr][nc][des] = dist[r][c][des] + 1
                q.append((nr,nc,des))
            elif des == 0 and a[nr][nc] == 1 and dist[nr][nc][1] == -1:
                dist[nr][nc][1] = dist[r][c][0] + 1
                q.append((nr,nc,1))
print(-1)