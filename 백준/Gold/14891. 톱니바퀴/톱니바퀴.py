import sys
from collections import deque
input = sys.stdin.readline

q = [deque(input().strip() ) for _ in range(4)]

ans = 0
k = int(input())
rotates = [list(map(int, input().split())) for _ in range(k)]

def rot(q):
    temp = q.pop()
    q.appendleft(temp)

def rotr(q):
    temp = q.popleft()
    q.append(temp)

for n, cl in rotates:
    rota = [0,0,0,0]
    rota[n-1] = cl

    for i in range(n-1,0,-1):
        if q[i-1][2] != q[i][6]:
            rota[i-1] = -rota[i]
        else:
            break
    for j in range(n-1,3):
        if q[j][2] != q[j+1][6]:
            rota[j+1] = -rota[j]
        else:
            break
    
    for u in range(4):
        if rota[u] == 1:
            rot(q[u])
        elif rota[u] == -1:
            rotr(q[u])


for p in range(4):
    if q[p][0] == '1':
        ans += 2 ** p

print(ans)