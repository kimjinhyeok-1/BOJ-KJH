import sys
input = sys.stdin.readline

r,c,t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]
d = [(1,0),(-1,0),(0,1),(0,-1)]

vacum = []
for x in range(r):
    if grid[x][0] == -1:
        vacum.append(x)

for _ in range(t):
    temp = [[0] * c for _ in range(r)] 
    for k in vacum:
        temp[k][0] = -1
    for i in range(r):
        for j in range(c):
            if grid[i][j] != 0 and grid[i][j] != -1: # 미세먼지가 존재하는 칸 찾기
                count = 0 # 미세먼지 주변에 공기청정기가 아닌 칸이 몇개 있는지 카운트 변수
                for di, dj in d:
                    ni,nj = i + di, j+dj
                    if 0<=ni<r and 0<= nj < c and grid[ni][nj] != -1: # 미세먼지 주변 칸이 grid를 벗어나지 않고 공기청정기가 아닐 때
                        count += 1
                        temp[ni][nj] += grid[i][j] // 5 # 주변에 5로 나누었을 때 정수 값 만큼 더해주기
                temp[i][j] += grid[i][j] - (grid[i][j] // 5) * count
    
    up = vacum[0]
    down = vacum[1]

    for i in range(up, 0, -1):
        temp[i][0] = temp[i-1][0]
    for j in range(0, c-1):
        temp[0][j] = temp[0][j+1]
    for i in range(0, up):
        temp[i][c-1] = temp[i+1][c-1]
    for j in range(c-1,0,-1):
        temp[up][j] = temp[up][j-1]
    temp[up][0] = -1
    temp[up][1] = 0

    for i in range(down, r-1):
        temp[i][0] = temp[i+1][0]
    for j in range(0,c-1):
        temp[r-1][j] = temp[r-1][j+1]
    for i in range(r-1, down,-1):
        temp[i][c-1] = temp[i-1][c-1]
    for j in range(c-1,1,-1):
        temp[down][j] = temp[down][j-1]
    temp[down][0] = -1
    temp[down][1] = 0
    grid = temp

ans = 0
for i in range(r):
    for j in range(c):
        if temp[i][j] != -1:
            ans += temp[i][j]

print(ans)