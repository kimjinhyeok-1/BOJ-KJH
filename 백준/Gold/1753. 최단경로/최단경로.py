import sys
import heapq
input = sys.stdin.readline
INF = 10**18

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist = [INF] * (V + 1)
dist[start] = 0

heap = []
heapq.heappush(heap, (0, start))

while heap:
    cur_dist, node = heapq.heappop(heap)

    if cur_dist > dist[node]:
        continue

    for v, w in graph[node]:
        new_dist = cur_dist + w
        if new_dist < dist[v]:
            dist[v] = new_dist
            heapq.heappush(heap, (new_dist, v))

ans = []
for i in range(1, V+1):
    if dist[i] == INF:
        ans.append('INF')
    else:
        ans.append(str(dist[i]))
print("\n".join(ans))