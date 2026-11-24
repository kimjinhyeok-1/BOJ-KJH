import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start, end):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, now = heapq.heappop(pq)

        if distance[now] < dist: continue

        for next_node, weight in graph[now]:
            cost = dist + weight
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))
    
    return distance[end]

u,v = map(int, input().split())

print(dijkstra(u,v))