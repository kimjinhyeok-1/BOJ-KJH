import sys
from collections import deque
input = sys.stdin.readline

n,m,t = map(int,input().split())
cas = [list(map(int, input().split())) for _ in range(n)]
dist = [[[-1, -1] for _ in range(m) ] for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

if cas[0][0] == 1 and cas[n-1][m-1] == 1: 
    print("Fail")
    sys.exit(0)

q = deque([(0,0,0)])
dist[0][0][0] = 0

while q:
    x,y,sw = q.popleft()
    cur = dist[y][x][sw]
    if x == m-1 and y == n-1:
        if cur <= t:
            print(cur)
            sys.exit(0)
    for dx, dy in d:
        nx,ny = x+dx, y+dy
        if not (0<=nx<m and 0<=ny<n): continue
        if sw ==0:
            if cas[ny][nx] == 0 and dist[ny][nx][sw] == -1:
                dist[ny][nx][sw] = cur + 1
                q.append((nx,ny,sw))
            elif cas[ny][nx] == 2 and dist[ny][nx][sw+1] == -1:
                dist[ny][nx][sw+1] = cur + 1
                q.append((nx,ny,sw+1))
        if sw==1:
            if dist[ny][nx][sw] == -1:
                dist[ny][nx][sw] = cur+1
                q.append((nx,ny,sw))
print("Fail")