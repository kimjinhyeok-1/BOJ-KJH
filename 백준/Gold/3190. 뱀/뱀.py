import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
apples = set(tuple(map(int, input().split())) for _ in range(k))
direc = [(0,1),(1,0),(0,-1),(-1,0)]
cur_d = 0
i = 0
cur_t = 0
l = int(input())
dire_ch = deque(list(input().split()) for _ in range(l))

cur_s = deque([(1,1)])
while True:
    cur_t += 1
    cx,cy = cur_s[0]
    dx,dy = direc[cur_d]
    nx,ny = cx+dx, cy+dy
    if (cur_d == 0 and ny == n+1) or (cur_d == 1 and nx == n+1) or (cur_d == 2 and ny == 0) or (cur_d == 3 and nx == 0) or (nx,ny) in cur_s:
        break
    cur_s.appendleft((nx,ny))
    if (nx,ny) not in apples:
        cur_s.pop()
    else:
        apples.remove((nx,ny))
    if dire_ch and cur_t == int(dire_ch[0][0]):
        t, dr = dire_ch.popleft()
        if dr == 'D':
            cur_d += 1
            if cur_d == 4: cur_d = 0
        elif dr == 'L':
            cur_d -= 1
            if cur_d == -1: cur_d = 3
print(cur_t)