import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
dist[0][0] = 1
q = deque([(0, 0)])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    a,b = q.popleft()
    
    for i in range(4):
        nx = a + dx[i]
        ny = b + dy[i]
        if 0<= nx < N and 0<= ny < M:
            if maze[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[a][b] + 1
                q.append((nx, ny))

print(dist[N-1][M-1])