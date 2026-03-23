import sys
from collections import deque
input = sys.stdin.readline
MAX = 100001
n,k = map(int, input().split())
dist = [-1] * MAX
parents = [-1] * MAX

q = deque([n])
dist[n] = 0

while q:
    a = q.popleft()
    if a == k:
        break
    if 0 <= a-1 < MAX and dist[a-1] == -1:
        dist[a-1] = dist[a] + 1
        parents[a-1] = a
        q.append(a-1)
    if 0 <= a+1 < MAX and dist[a+1] == -1:
        dist[a+1] = dist[a] + 1
        parents[a+1] = a
        q.append(a+1)
    if 0<= a*2 < MAX and dist[a*2] == -1:
        dist[a*2] = dist[a] + 1
        parents[a*2] = a
        q.append(a*2)

results = []
idx = k
while idx != -1:
    results.append(idx)
    if idx == n:
        break
    idx = parents[idx]
print(dist[k])
print(" ".join(map(str, results[::-1])))