import sys
from collections import deque
input = sys.stdin.readline

N,M,K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
dist = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)] # 접근 시 dist[N][M][K]
d = [(1,0),(-1,0),(0,1),(0,-1)]


dist[0][0][0] = 1
q = deque([(0,0,0)])

while q:
    
    x,y,broken = q.popleft()
    cur = dist[y][x][broken]
    if x == M-1 and y == N-1:
        print(dist[y][x][broken])
        sys.exit(0)
    for dx, dy in d:
        nx,ny = x+dx, y+dy
        if not (0<=nx<M and 0<=ny<N):
            continue
        if grid[ny][nx] == 0 and dist[ny][nx][broken] == -1:
            dist[ny][nx][broken] = cur + 1
            q.append((nx,ny,broken))
        elif grid[ny][nx] == 1 and broken<K and dist[ny][nx][broken+1] == -1:
            dist[ny][nx][broken + 1] = cur + 1
            q.append((nx,ny,broken + 1))
print(-1)