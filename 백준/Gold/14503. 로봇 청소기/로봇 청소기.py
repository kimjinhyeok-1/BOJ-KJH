import sys
input = sys.stdin.readline

n,m = map(int, input().split())
r,c,di = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
ans = 0

while True:
    if grid[r][c] == 0:
        ans += 1
        grid[r][c] = 2
    
    cleaned = True
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0<= nr < n and 0<= nc < m:
            if grid[nr][nc] == 0:
                cleaned = False
    if cleaned:
        back = (di+2) % 4
        nr, nc = r + d[back][0], c + d[back][1]
        if grid[nr][nc] == 2:
            r,c = nr, nc
        else:
            print(ans)
            sys.exit(0)
    else:
        # 0 -> 3 1->0 2->1
        di = (di+3) % 4
        nr,nc = r+d[di][0], c+d[di][1]
        if 0<=nr< n and 0<= nc < m and grid[nr][nc] == 0:
            r,c = nr, nc

