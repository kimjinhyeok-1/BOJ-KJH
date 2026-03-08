import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
ans = 0
cnt = 0

def bfs(n,m):
    dist[n][m] = 1
    q = deque([(n,m)])
    temp = 1
    while q:
        a,b = q.popleft()     
        for da,db in d:
            na,nb = a+da,b+db
            if 0<=na<r and 0<=nb<c:
                if grid[na][nb] == 1 and dist[na][nb] == -1:
                    temp+=1
                    dist[na][nb] = 1
                    q.append((na,nb))
    return temp



for i in range(r):
    for j in range(c):
        if grid[i][j] == 1 and dist[i][j] == -1:
            t = bfs(i,j)
            ans = max(ans,t)
            cnt += 1

print(cnt)
print(ans)