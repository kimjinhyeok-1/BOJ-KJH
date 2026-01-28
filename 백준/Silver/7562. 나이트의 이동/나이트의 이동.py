import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

for _ in range(T):
    l = int(input())
    sx, sy = map(int, input().split())
    tx, ty = map(int, input().split())
    dist = [[-1] * l for _ in range(l)]
    dist[sx][sy] = 0
    q = deque([(sx, sy)])
    while q:
        a, b = q.popleft()
        if a == tx and b == ty:
            print(dist[a][b])
            break
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<= nx < l and 0<= ny < l:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[a][b] + 1
                    q.append((nx, ny))
        