import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
move = [0] * 101

for _ in range(n+m):
    a,b = map(int, input().split())
    move[a] = b

dist = [-1] * 101
q = deque([1])
dist[1] = 0

while q:
    x = q.popleft()
    for dx in range(1,7):
        nx = x + dx
        if nx > 100:
            continue
        if move[nx] != 0:
            nx = move[nx]
        if dist[nx] == -1:
            dist[nx] = dist[x] + 1
            q.append(nx)

print(dist[100])