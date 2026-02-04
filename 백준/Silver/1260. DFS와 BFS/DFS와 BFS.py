import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int, input().split())
stack = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    stack[a].append(b)
    stack[b].append(a)
for i in range(n+1):
    stack[i].sort()

visited = [False] * (n+1)
def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for nx in stack[v]:
        if visited[nx] == False:
            dfs(nx)
dfs(v)
print()

visited = [False] * (n+1)
q = deque([v])
visited[v] = True

while q:
    k = q.popleft()
    print(k, end = ' ')
    for nx in stack[k]:
        if visited[nx] == False:
            visited[nx] = True
            q.append(nx)
print()