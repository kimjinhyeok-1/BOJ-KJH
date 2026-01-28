import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

q = deque()
for x in range(N):
    for y in range(M):
        if tomato[x][y] == 1:
            dist[x][y] = 0
            q.append((x,y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    a,b = q.popleft()
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        
        if 0<= nx < N and 0<= ny < M:
            if tomato[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[a][b] + 1
                tomato[nx][ny] = 1
                q.append((nx, ny))

ans = 0
for x in range(N):
    for y in range(M):
        if tomato[x][y] == 0:
            print(-1)
            exit()
        elif dist[x][y] > ans:
            ans = dist[x][y]
            
print(ans)