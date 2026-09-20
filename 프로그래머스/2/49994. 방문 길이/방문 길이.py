def solution(dirs):
    answer = 0
    d = {"U": (-1,0),"D": (1,0),"L": (0,-1),"R": (0,1)}
    r, c = 5, 5
    visited = set()
    
    for di in dirs:
        dr, dc = d[di]
        nr, nc = r + dr, c  + dc
        
        # 범위를 벗어났는지 먼저 확인
        if not(0 <= nr <= 10 and 0 <= nc <= 10):
            continue
        
        path = ((r,c), (nr,nc))
        reversed_path = ((nr, nc), (r,c))
        
        if path not in visited:
            answer += 1
            visited.add(path)
            visited.add(reversed_path)

        r, c = nr, nc
        
        
    return answer