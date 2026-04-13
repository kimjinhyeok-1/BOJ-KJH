import sys
input = sys.stdin.readline
MAX = 10**18

# 0: 위,1: 아래,2: 오른쪽,3:왼쪽 
dr = [-1,1,0,0]
dc = [0,0,1,-1]

cctv_dir ={
    1: [[0],[1],[2],[3]],
    2: [[2,3],[0,1]],
    3: [[0,2],[2,1],[1,3],[3,0]],
    4: [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    5: [[0,1,2,3]]
}

N,M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
result = MAX

cctv = []
for i in range(N):
    for j in range(M):
        if grid[i][j] in (1,2,3,4,5):
            # cctv라면 행,열,종류를 cctv 배열에 추가
            cctv.append((i,j,grid[i][j]))

def watch(r,c,directions):
    changed = []
    # 각 방향에서 하나씩 돌아가면서 감시 처리
    for d in directions:
        nr,nc = r,c
        while True:
            nr += dr[d]
            nc += dc[d]
            
            # 만약 다음 칸이 범위를 벗어나거나 벽이면 break
            if not(0<=nr<N and 0<= nc<M):
                break
            if grid[nr][nc] == 6:
                break
            # 0 이라면 감시처리 후 changed 배열에 저장 -> 나중에 다시 0으로 바꾸기 위함
            if grid[nr][nc] == 0:
                grid[nr][nc] = '#'
                changed.append((nr,nc))
    
    return changed




def dfs(depth):
    global result
    # 만약 깊이가 cctv 배열 길이와 같다면 한가지 경우가 완료된 경우이므로 0(사각지대) 개수를 세고 result와 비교하여 작으면 업데이트
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
        return

    r, c, type = cctv[depth]
    for directions in cctv_dir[type]:
        changed = watch(r,c,directions)
        dfs(depth + 1)

        for i,j in changed:
            grid[i][j] = 0

dfs(0)
print(result)