import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

d = [(1,0),(-1,0),(0,1),(0,-1)]
grid = [list(map(int, input().split())) for _ in range(n)]
ma = 0
for i in range(n):
    for j in range(n):
        ma = max(ma,grid[i][j])
def bfs(q, k, visited): # k 이하는 모두 잠긴다 의미
    while q:
        r,c = q.popleft()
        for dr, dc in d:
            nr,nc = r+dr, c+dc
            if 0<= nr < n and 0 <= nc < n:
                if grid[nr][nc] > k and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc))

ans = 0
for k in range(ma):
    temp = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] > k and not visited[i][j]:
                q = deque([(i,j)])
                visited[i][j] = True
                bfs(q, k, visited)
                temp += 1
    ans = max(ans, temp)

print(ans)