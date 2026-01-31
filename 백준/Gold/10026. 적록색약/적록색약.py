import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
colors = [list(input().strip()) for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
visited = [[False] * N for _ in range(N)]
count1, count2 = 0,0
def bfs(x,y):
    visited[y][x] = True
    color = colors[y][x]
    q = deque([(x,y)])
    while q:
        sx, sy = q.popleft()
        for dx, dy in d:
            nx, ny = sx + dx, sy + dy
            if 0<= nx < N and 0<= ny < N:
                if colors[ny][nx] == color and not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((nx,ny))

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(x,y)
            count1 += 1

for y in range(N):
    for x in range(N):
        if colors[y][x] == 'G':
            colors[y][x] = 'R'

visited = [[False] * N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(x,y)
            count2 += 1
print(count1 , count2)