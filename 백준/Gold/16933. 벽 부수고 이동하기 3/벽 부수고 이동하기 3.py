import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [input().strip() for  _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)] # 접근을 dist[N][M][K]로 접근
d = [(1,0),(-1,0),(0,1),(0,-1)]

q = deque([(0,0,0)])
visited[0][0][0] = True

dist = 1

while q:
    for _ in range(len(q)):
        r,c,k = q.popleft()
        if r == N-1 and c == M-1:
            print(dist)
            sys.exit(0)
        is_day = dist % 2
        need_wait = False
        for dr, dc in d:
            nr, nc = r +dr, c+dc
            if 0<= nr < N and 0 <= nc < M:
                if grid[nr][nc] == '0' and not visited[nr][nc][k]:
                    visited[nr][nc][k] = True
                    q.append((nr,nc,k))
                elif grid[nr][nc] == '1' and k<K:
                    if is_day and not visited[nr][nc][k+1]:
                        visited[nr][nc][k+1] = True
                        q.append((nr,nc,k+1))
                    elif is_day == 0:
                        need_wait = True
        if need_wait:
            q.append((r,c,k))
    dist += 1

print(-1)