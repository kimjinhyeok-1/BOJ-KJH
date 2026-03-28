import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
d = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(T):
    m,n,k = map(int, input().split())
    grid = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    count = 0

    for _ in range(k):
        j,i = map(int, input().split())
        grid[i][j] = 1

    def bfs(q):
        while q:
            r,c = q.popleft()
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if 0<= nr< n and 0<= nc < m and grid[nr][nc] == 1 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr,nc))
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == 1:
                visited[i][j] = True
                q = deque([(i,j)])
                bfs(q)
                count += 1
    

    print(count)