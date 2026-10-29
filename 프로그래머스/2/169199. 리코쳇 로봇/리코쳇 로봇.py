from collections import deque

def solution(board):  
    answer = 0
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    N = len(board)
    M = len(board[0])
    q = deque()
    visited = [[-1] * M for _ in range(N)]
    
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'R':
                q.append((r,c))
                visited[r][c] = 0
            
                
    while q:
        r,c = q.popleft()
        if board[r][c] == 'G':
            return visited[r][c]
        for dr, dc in directions:
            nr, nc = r, c
            while 0<=nr<N and 0<=nc<M and board[nr][nc] != 'D':
                nr += dr
                nc += dc
            nr, nc = nr - dr, nc - dc
            if visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr,nc))
    return -1