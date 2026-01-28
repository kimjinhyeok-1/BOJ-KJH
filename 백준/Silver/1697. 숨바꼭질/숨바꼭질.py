import sys
from collections import deque
input = sys.stdin.readline
MAX = 100000
dist = [-1] * (MAX + 1)
n,k = map(int, input().split())

dist[n] = 0
q = deque([n])
while q:
    v = q.popleft()
    if v == k:
        print(dist[v])
        break
    for nxt in (v-1, v+1, v*2):
        if 0<= nxt <= MAX and dist[nxt] == -1:
            dist[nxt] = dist[v] + 1
            q.append(nxt)
