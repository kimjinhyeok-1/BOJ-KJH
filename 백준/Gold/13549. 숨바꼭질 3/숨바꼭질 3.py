import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int, input().split())

MAX = 100001
INF = 10 ** 9
dist = [INF] * MAX

dist[n] = 0
q = deque([n])

while q:
    x = q.popleft()
    if x == k:
        print(dist[k])
        break
    nx = x*2
    if 0<= nx < MAX and dist[nx] > dist[x]:
        dist[nx] = dist[x]
        q.appendleft(nx)
    
    nx = x+1
    if 0<= nx < MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x] + 1
        q.append(nx)
    
    nx = x-1
    if 0<= nx < MAX and dist[nx] > dist[x] + 1:
        dist[nx] = dist[x]+1
        q.append(nx)