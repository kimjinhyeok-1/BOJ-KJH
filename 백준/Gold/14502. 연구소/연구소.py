import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

empty = []
virus = []
d = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0

for y in range(N):
    for x in range(M):
        if grid[y][x] == 0:
            empty.append((x,y))
        elif grid[y][x] == 2:
            virus.append((x,y))

def spread(temp):
    q = deque(virus)
    while q:
        ix, iy = q.popleft()
        for dx, dy in d:
            nx, ny = ix + dx, iy + dy
            if 0<= nx < M and 0<= ny < N and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append((nx,ny))

E = len(empty)
for i in range(E):
    for j in range(i+1, E):
        for k in range(j+1, E):
            w1, w2, w3 = empty[i], empty[j], empty[k] # 벽 세울 3곳 정해서 (x,y) 좌표 넣음.
            temp = [row[:] for row in grid]
            for x,y in (w1, w2, w3): temp[y][x] = 1

            spread(temp)
            safe = 0
            for y in range(N):
                for x in range(M):
                    if temp[y][x] == 0: safe += 1
            ans = max(ans, safe)

print(ans)