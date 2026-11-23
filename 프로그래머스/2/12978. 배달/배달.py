import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for a, b, cost in road:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0

    pq = [(0, 1)]

    while pq:
        current_dist, current = heapq.heappop(pq)

        if current_dist > dist[current]:
            continue

        for nxt, cost in graph[current]:
            new_dist = current_dist + cost

            if new_dist < dist[nxt]:
                dist[nxt] = new_dist
                heapq.heappush(pq, (new_dist, nxt))

    answer = 0

    for d in dist[1:]:
        if d <= K:
            answer += 1

    return answer