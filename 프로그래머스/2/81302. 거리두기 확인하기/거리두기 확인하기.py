from collections import deque

def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    
    return answer

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if not bfs(place, r, c):
                    return 0
    return 1

def bfs(place, sr, sc):
    q = deque([(sr, sc, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[sr][sc] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        r, c, dist = q.popleft()
        
        if dist >= 2:
            continue
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if not (0<= nr < 5 and 0<= nc < 5):
                continue
            if visited[nr][nc]:
                continue

            if place[nr][nc] == 'X':
                continue

            if place[nr][nc] == 'P':
                return False

            visited[nr][nc] = True
            q.append((nr, nc, dist + 1))

    return True