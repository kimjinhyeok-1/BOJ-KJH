import sys
from collections import deque
input = sys.stdin.readline

c,r = map(int,input().split())

t = [list(map(int,input().split())) for _ in range(r)]
dist = [[-1] * c for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque()

for i in range(r):
    for j in range(c):
        if t[i][j] == 1:
            dist[i][j] = 0
            q.append((i,j))

while q:
    a,b = q.popleft()
    for da, db in d:
        na,nb = a+da,b+db
        if 0<=na<r and 0<=nb<c and t[na][nb] == 0 and dist[na][nb] == -1:
            dist[na][nb] = dist[a][b] + 1
            t[na][nb] = 1
            q.append((na,nb))


ans = 0
for p in range(r):
    for k in range(c):
        if t[p][k] == 0:
            print(-1)
            exit()
        else:
            ans = max(dist[p][k], ans)


print(ans)