"""
매년 주위의 바다 개수만큼 빙산이 줄어듦
** 매년 해야되는 것**
1. 주위 바다 개수 체크해서 다른 temp 배열을 하나씩 만들기 -> 1년 후의 배열이 temp에 저장
2. 해당 temp가 최소 두 개 이상의 덩어리로 분리가 되었는지 bfs로 확인
"""
import sys
from collections import deque
input = sys.stdin.readline
d = [(0,1),(0,-1),(1,0),(-1,0)]

answer = 0
N,M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]

def bfs(n):

    return

def check_ocean(r,c,grid):
    temp = 0

    for dr, dc in d:
        nr,nc = r+dr, c+dc
        if grid[nr][nc] == 0:
            temp += 1
    
    return (grid[r][c] - temp) if (grid[r][c] - temp) > 0 else 0

while True:
    answer += 1
    temp = [[0] * M for _ in range(N)]

    for r in range(1,N-1):
        for c in range(1,M-1):
            temp[r][c] = check_ocean(r,c,ice)
    
    visited = [[False] * M for _ in range(N)]
    count = 0
    for r in range(1,N-1):
        for c in range(1, M-1):
            if not visited[r][c] and temp[r][c] != 0:
                visited[r][c] = True
                q = deque([(r,c)])

                while q:
                    rr, cc  = q.popleft()
                    for dr, dc in d:
                        nr, nc = rr + dr, cc + dc
                        if not (0<=nr<N and 0<=nc<M):
                            continue
                        if not visited[nr][nc] and temp[nr][nc] != 0:
                            visited[nr][nc] = True
                            q.append((nr,nc))
                count += 1
    ice = temp
    if count >= 2:
        print(answer)
        break

    if count == 0:
        print(0)
        break