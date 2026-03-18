import sys
input = sys.stdin.readline

n,m = map(int, input().split())

ans = 0
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(r,c,depth,v):
    global ans
    if depth == 4:
        ans = max(ans, v)
        return
    for dr, dc in d:
        nr, nc = r+dr,c+dc
        if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr,nc,(depth +1), (v+grid[nr][nc]))
            visited[nr][nc] = False
        
def other(r,c,v):
    arr = []
    for dr,dc in d:
        nr,nc = r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            arr.append(grid[nr][nc])
    l = len(arr)
    if l < 3:
        return 0
    elif l == 3:
        v = v + sum(arr)
    else:
        v = v + sum(arr) - min(arr)
        
    return v




for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r,c,1,grid[r][c])
        visited[r][c] = False
        temp2 = other(r,c,grid[r][c])
        ans = max(ans,temp2)

print(ans)