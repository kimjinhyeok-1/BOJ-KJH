import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
r1,c1,r2,c2 = map(int, input().split())

d = [(-2,-1), (-2,1), (0,-2), (0,2), (2,-1), (2,1)]
dist = [[-1] * n for _ in range(n)]

q = deque([(r1,c1)])
dist[r1][c1] = 0

while q:
    r,c = q.popleft()
    if r == r2 and c == c2:
        print(dist[r][c])
        sys.exit(0)
    for dr,dc in d:
        nr,nc = r+dr,c+dc
        if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr,nc))
print(-1)
'''
-1 -1 -1 +3 -1 +3 -1
-1 -1 +3 -1 -1 -1 +3
-1 +3 -1 -1 +2 -1 +2
+3 -1 -1 +2 -1 +2 -1
-1 +3 +2 +3 -1 +1 -1
+3 -1 -1 +2 +1 -1 -1
-1 -1 +2 -1 -1 +3  0

'''