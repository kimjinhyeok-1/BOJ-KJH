import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]

water_q = deque()
go_q = deque()
dist = [[-1] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if grid[r][c] == "*":
            water_q.append((r,c))
        elif grid[r][c] == 'S':
            go_q.append((r,c))
            dist[r][c] = 0

d = [(1,0),(-1,0),(0,1),(0,-1)]

while go_q:
    for _ in range(len(water_q)):
        wr, wc = water_q.popleft()
        for dwr, dwc in d:
            nwr, nwc = wr + dwr, wc + dwc
            if 0<=nwr<n and 0<=nwc<m and grid[nwr][nwc] == '.':
                grid[nwr][nwc] = "*"
                water_q.append((nwr,nwc))
    for _ in range(len(go_q)):
        gr, gc = go_q.popleft()
        for dgr, dgc in d:
            ngr, ngc = gr + dgr, gc + dgc
            if 0<=ngr<n and 0<=ngc<m:
                if grid[ngr][ngc] == 'D':
                    print(dist[gr][gc] + 1)
                    exit(0)
                if  grid[ngr][ngc] == '.' and dist[ngr][ngc] == -1:
                    dist[ngr][ngc] = dist[gr][gc] + 1
                    go_q.append((ngr,ngc))
print('KAKTUS')