import sys 
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
stack = [[] for _ in range(n+1)]
for _ in range(1, m+1):
    a, b = map(int, input().split())
    stack[a].append(b)
    stack[b].append(a)
for i in range(1,n+1):
    stack[i].sort()

visited = [False] * (n+1)
count = 0
q = deque()

    
for i in range(1,n+1):
    if visited[i] == False:
        q.append(i)
        visited[i] = True
        while q:
            v = q.popleft()
            for nx in stack[v]:
                if visited[nx] == False:
                    visited[nx] = True
                    q.append(nx)
        count += 1
print(count)