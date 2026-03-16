import sys
from collections import deque
input = sys.stdin.readline

n,l,rr = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
while True:
    moved = False
    vi = [[False] * n for _ in range(n)]
    q = deque()
    
    for r in range(n):
        for c in range(n):
            cnt = 1
            su = 0
            union = [(r,c)]
            if not vi[r][c]:
                q.append((r,c))
                vi[r][c] = True
                su = grid[r][c]
                while q:
                    a, b = q.popleft()
                    for da,db in d:
                        na,nb = a+da,b+db
                        if 0<=na<n and 0<= nb<n:
                            if not vi[na][nb] and l <= abs(grid[a][b] - grid[na][nb]) <= rr:
                                vi[na][nb] = True
                                su += grid[na][nb]
                                cnt += 1
                                q.append((na,nb))
                                union.append((na,nb))
            if cnt >= 2:
                moved = True
                for y,x in union:
                    grid[y][x] = su // cnt
    
    if moved:
        ans += 1
    elif not moved:
        break

print(ans)