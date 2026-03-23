import sys
from collections import deque
input = sys.stdin.readline
s = int(input())
MAX = 1001
q = deque([(1,0)])
dist = [[-1] * MAX for _ in range(MAX)]
dist[1][0] = 0

while q:
    cs, clip = q.popleft()
    if cs == s:
        print(dist[cs][clip])
        sys.exit(0)
    if dist[cs][cs] == -1:
        dist[cs][cs] = dist[cs][clip] + 1
        q.append((cs,cs))
    if clip >0 and cs + clip < MAX and dist[cs+clip][clip] == -1:
        dist[cs+clip][clip] = dist[cs][clip] + 1
        q.append((cs+clip, clip))
    if cs>0 and dist[cs-1][clip] == -1:
        dist[cs-1][clip] = dist[cs][clip] + 1
        q.append((cs-1, clip))
    