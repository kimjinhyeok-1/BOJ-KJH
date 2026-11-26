"""
1. 주사위는 지도 위에 윗 면이 1 동쪽 가리키는 방향이 3 놓인 곳은 (x,y), 모든 면이 0
2. 굴렸을 때 칸이 0이면 주사위 숫자가 칸에 복사, 0이 아니면 칸 숫자가 주사위에 복사
3. 동쪽은 1, 서쪽은2, 북쪽은 3, 남쪽은 4

초기값 설정해야되는 것: 6면의 값들 저장하는 변수 6개 
만들어야 되는 함수: 동서남북 4방향으로 굴렸을 때 바뀌는 면들 계산
"""

import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
grid = []
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(N):
    grid.append(list(map(int, input().split())))

# 6개의 변수에 값들 
top = 0
bottom = 0
east = 0
west = 0
north = 0
south = 0

# 굴리는 함수
def roll(dir):
    # 전역 변수로 선언해줘야 밖에 있느 값들이 바뀜
    global top, bottom, east, west, north, south

    if dir == 1:
        temp = east
        east = top
        top = west
        west = bottom
        bottom = temp
    elif dir == 2:
        temp = west
        west = top
        top = east
        east = bottom
        bottom = temp
    elif dir == 3:
        temp = north
        north = top
        top = south
        south = bottom
        bottom = temp
    else:
        temp = south
        south = top
        top = north
        north = bottom
        bottom = temp

seq = list(map(int, input().split()))

for i in range(K):
    dir = seq[i]
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < N and 0 <= ny < M):
        continue

    x,y = nx,ny
    roll(dir)

    # 굴렸는데 칸의 숫자가 0인 경우
    if  grid[x][y] == 0:
        grid[x][y] = bottom
    
    # 굴렸는데 칸의 숫자가 0이 아닌 경우
    else:
        bottom = grid[x][y]
        grid[x][y] = 0
    
    print(top)