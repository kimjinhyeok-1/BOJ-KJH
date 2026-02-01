import sys 
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
grid = [list(map(int,input().strip())) for _ in range(N)]
dist = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque([(0,0,0)])
dist[0][0][0] = 1

while q:
    x,y,z = q.popleft()
    if x == M-1 and y == N-1:
        print(dist[y][x][z])
        exit()
    for dx, dy in d:
        nx, ny = x+dx, y+dy
        if 0<=nx<M and 0<=ny<N and grid[ny][nx] == 0 and dist[ny][nx][z] == -1:
            dist[ny][nx][z] = dist[y][x][z] + 1
            q.append((nx,ny,z))
        elif 0<=nx<M and 0<=ny<N and z == 0 and grid[ny][nx] == 1 and dist[ny][nx][1] == -1:
            dist[ny][nx][1] = dist[y][x][0] + 1
            q.append((nx,ny,1))

print(-1)
