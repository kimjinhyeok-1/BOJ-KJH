import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
maxG = max(map(max, grid))

answer = 0

for h in range(maxG):
    cnt = 0
    d = [(-1, 0),(1, 0),(0, 1),(0, -1)]
    visited = [[False] * N for _ in range(N)]
    def bfs(x,y):
        visited[y][x] = True
        q = deque([(x,y)])
        while q:
            ix,iy = q.popleft()
            for dx, dy in d:
                nx = ix + dx
                ny = iy + dy
                if 0<= nx < N and 0<= ny < N and not visited[ny][nx] and grid[ny][nx] > h:
                    visited[ny][nx] = True
                    q.append((nx,ny))
    for y in range(N):
        for x in range(N):
            if grid[y][x] > h and not visited[y][x]:
                bfs(x,y)
                cnt += 1
    answer = max(answer, cnt)  

print(answer)