import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
houseCnt = []
def bfs(x,y):
    cnt = 1
    visited[y][x] = True
    q = deque([(x,y)])
    while q:
        ix, iy = q.popleft()
        for dx, dy in d:
            nx = ix + dx
            ny = iy + dy
            if 0<= nx < N and 0<= ny < N and not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                q.append((nx,ny))
                cnt += 1
    houseCnt.append(cnt)

for y in range(N):
    for x in range(N):
        if grid[y][x] == 1 and not visited[y][x]:
            bfs(x,y)

print(len(houseCnt))
houseCnt.sort()
for x in houseCnt:
    print(x)