from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(0,n-1):
        for j in range(i+1,n):
            print(i,j)
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
    for i in range(n):
        graph[i].sort()
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            q = deque([(i)])
            while q:
                nxt = q.popleft()
                for v in graph[nxt]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)
            answer += 1
    return answer
