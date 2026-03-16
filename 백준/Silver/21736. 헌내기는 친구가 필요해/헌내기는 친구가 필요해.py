import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
ans = 0
campus = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque()

for r in range(n):
    for c in range(m):
        if campus[r][c] == 'I':
            q.append((r,c))
            visited[r][c] = True

while q:
    r,c = q.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0<=nr<n and 0<=nc<m:
            nv = campus[nr][nc]
            if  nv == "X":
                continue
            if not visited[nr][nc] :
                if nv == 'O':
                    visited[nr][nc] = True
                    q.append((nr,nc))
                elif nv == 'P':
                    visited[nr][nc] = True
                    ans += 1
                    q.append((nr,nc))

if ans == 0: 
    print('TT')
else:
    print(ans)