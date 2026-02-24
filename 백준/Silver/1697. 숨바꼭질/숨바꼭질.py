import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())
MAX = 1000000

dist = [-1] * (MAX+1)
dist[n] = 0
q = deque([n])

while q:
    x = q.popleft()
    for nx in (x-1, x+1, x*2):
        if 0<= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)
print(dist[k])