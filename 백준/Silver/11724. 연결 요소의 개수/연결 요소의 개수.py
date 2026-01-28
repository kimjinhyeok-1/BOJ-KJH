import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    visited[v] = True
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

count = 0
for v in range(1, n+1):
    if not visited[v]:
        dfs(v)
        count += 1

print(count)