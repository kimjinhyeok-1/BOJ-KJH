import sys
input = sys.stdin.readline
n,m = map(int, input().split())

ans = 0
ds = [[(0,1),(0,2),(0,3)], [(1,0),(2,0),(3,0)], # ㅡ 모양 ㅣ 모양
      
     [(1,0),(0,1),(1,1)], # ㅁ 모양

     [(1,0),(2,0),(2,1)], [(0,1),(0,2),(-1,2)], # L 모양 (회전 포함 8개)
     [(0,1),(1,1),(2,1)], [(1,0),(1,1),(1,2)],

     [(0,1),(-1,1),(-2,1)], [(0,1),(0,2),(1,2)],
     [(0,1),(1,0),(2,0)], [(1,0),(0,1),(0,2)],

     [(0,-1),(0,1),(1,0)], [(0,-1),(1,0),(-1,0)], # ㅗ 모양 (회전 포함 4개)
     [(0,-1),(0,1),(-1,0)], [(0,1),(1,0),(-1,0)],

     [(1,0),(1,1),(2,1)], [(0,1),(-1,1),(-1,2)], # 번개모양 (회전 포함 4개)
     [(1,0),(0,1),(-1,1)], [(0,1),(1,1),(1,2)] 
     ]

grid  = [list(map(int, input().split())) for _ in range(n)]

def bfs(r,c,d):
    temp = grid[r][c]

    for dr, dc in d:
        nr,nc = r + dr, c + dc
        if nr<0 or nr>=n or nc<0 or nc>=m:
            return 0
        else:
            temp += grid[nr][nc]
    return temp


for r in range(n):
    for c in range(m):
        for d in ds:
            ans = max(ans, bfs(r,c,d))

print(ans)