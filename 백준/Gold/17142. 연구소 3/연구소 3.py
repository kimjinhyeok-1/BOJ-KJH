import sys
from collections import deque
input =  sys.stdin.readline

MAX = 10**18
ans = MAX
n,m = map(int, input().split())
d = [(1,0),(-1,0),(0,1),(0,-1)]
dist = [[-1] * n for _ in range(n)]
grid = [list(map(int, input().split())) for _ in range(n)]

virus = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            virus.append((i,j))

len_virus = len(virus)
active_virus = []
def backtraking(start, depth):
    if depth == m:
        bfs(active_virus)
        return
    for i in range(start,len_virus):
        active_virus.append(virus[i])
        backtraking(i+1, depth+1)
        active_virus.pop()


def bfs(virus):
    global ans
    q = deque(virus)
    dist = [[-1] * n for _ in range(n)]

    for r,c in virus:
        dist[r][c] = 0
    while q:
        for _ in range(len(q)):
            r,c = q.popleft()
            for dr,dc in d:
                nr,nc = r+dr, c+dc
                if 0<= nr < n and 0<= nc < n:
                    if dist[nr][nc] == -1 and grid[nr][nc] != 1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr,nc))

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0 and dist[i][j] == -1:
                return
    
    max_time = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                max_time = max(max_time, dist[i][j])

    ans = min(ans, max_time)
    

 


backtraking(0,0)
if ans == MAX:
    print(-1)
    sys.exit()
print(ans)
'''
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
'''