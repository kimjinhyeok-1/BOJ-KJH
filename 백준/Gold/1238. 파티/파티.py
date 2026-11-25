import sys
import heapq

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))
    reverse_graph[b].append((a, cost))

def dijkstra(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, now = heapq.heappop(pq)

        if current_dist > dist[now]: 
            continue

        for nxt, cost in graph[now]:
            new_dist = current_dist + cost

            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))
    
    return dist

from_x = dijkstra(X, graph)
to_x = dijkstra(X, reverse_graph)

answer = 0

for i in range(1, N+1):
    answer = max(answer, (from_x[i] + to_x[i]))


print(answer)