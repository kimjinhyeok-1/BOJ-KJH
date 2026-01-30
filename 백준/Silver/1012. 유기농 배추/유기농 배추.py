import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    v = [[0] * M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        v[b][a] = 1
    d = [(1,0), (-1,0),(0,1),(0,-1)]
    def bfs(x, y):
        v[y][x] = 0
        q = deque([(x, y)])
        while q:
            sx, sy = q.popleft()
            for a, b in d:
                nx = sx + a
                ny = sy + b
                if 0 <= nx < M and 0<= ny < N and v[ny][nx] == 1:
                    v[ny][nx] = 0
                    q.append((nx, ny))
    
    count = 0
    for i in range(N):
        for j in range(M):
            if v[i][j] == 1:
                bfs(j,i)
                count += 1
    print(count)    