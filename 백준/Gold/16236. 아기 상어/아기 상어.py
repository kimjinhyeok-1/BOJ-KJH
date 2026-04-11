import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

eat_count = 0
x,y,size = 0,0,2
time = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 9:
            x,y = i,j
            grid[i][j] = 0

def eat(x,y,size):
    visited = [[-1] * n for _ in range(n)]
    temp = []
    q = deque()
    q.append((x,y))
    visited[x][y] = 0
    while q:
        r,c = q.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if 0<= nr<n and 0<= nc<n:
                if grid[nr][nc] <= size and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr,nc))
                    if grid[nr][nc] < size and grid[nr][nc] != 0:
                        temp.append((nr,nc,visited[nr][nc]))
    if not temp:
        return None
    temp.sort(key=lambda x:(x[2], x[0], x[1]))
    return temp[0]

while True:
    target = eat(x,y,size)
    if target:
        nx,ny,dist = target
        time += dist
        grid[nx][ny] = 0
        eat_count += 1
        x,y = nx, ny
    else:
        break

    if eat_count == size:
        eat_count = 0
        size += 1
    
print(time)