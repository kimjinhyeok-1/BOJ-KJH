import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
INF = 10**9

d = [(1,0),(-1,0),(0,1),(0,-1)]

def bfs(r,c):
    temp = [[INF] * (w+2) for _ in range(h+2)]
    temp[r][c] = 0
    q = deque([(r,c)])
    while q:
        a,b = q.popleft()
        for da, db in d:
            na, nb = a+da, b+db
            if 0<= na< h+2 and 0<= nb < w+2 and grid[na][nb] != '*':
                n_v = temp[a][b] + (1 if grid[na][nb] == '#' else 0)
                if n_v < temp[na][nb]:
                    temp[na][nb] = n_v
                    if grid[na][nb] == '.':
                        q.append((na,nb))
                    elif grid[na][nb] == '#':
                        q.append((na,nb))
    return temp

for _ in range(T):
    h, w = map(int, input().split())
    grid = [list('.' * (w+2))]
    for i in range(h):
        grid.append(list('.' + input().strip() + '.' ))
    grid.append(list('.' * (w+2)))
    prisoner = []
    for i in range(h+2):
        for j in range(w+2):
            if grid[i][j] == '$':
                grid[i][j] = '.'
                prisoner.append((i,j))
    temp0 = bfs(0,0)
    temp1 = bfs(prisoner[0][0], prisoner[0][1])
    temp2 = bfs(prisoner[1][0], prisoner[1][1])

    ans = INF
    for i in range(h+2):
        for j in range(w+2):
            if temp0[i][j] != INF and temp1[i][j] != INF and temp2[i][j] != INF and grid[i][j] != '*':
                tans = temp0[i][j] + temp1[i][j] + temp2[i][j]
                if grid[i][j] == '#':
                    tans -= 2
                ans = min(ans, tans)
    print(ans)