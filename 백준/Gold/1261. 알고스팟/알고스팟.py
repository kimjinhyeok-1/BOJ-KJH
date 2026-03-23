import sys
from collections import deque
input = sys.stdin.readline

MAX = 10001
c, r = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(r)]
dist = [[MAX] * c for _ in range(r)]
dist[0][0] = 0
d = [(1,0),(-1,0),(0,1),(0,-1)]
q = deque([(0,0)])

while q:
    a,b = q.popleft()
    
    for da,db in d:
        na,nb = a+da, b+ db
        if 0<= na < r and 0<= nb < c:
            new_cost = dist[a][b] + grid[na][nb]
            if new_cost < dist[na][nb]:
                dist[na][nb] = new_cost
                if grid[na][nb] == 0:
                    q.append((na,nb))
                else:
                    q.append((na,nb))

print(dist[r-1][c-1])
        