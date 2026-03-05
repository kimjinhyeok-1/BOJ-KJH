import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

g = [list(input().strip()) for _ in range(n)]

f = deque()
j = deque()
dist = [[-1] * m for _ in range(n)]

for p in range(n):
    for k in range(m):
        if g[p][k] == 'J':
            j.append((p,k))
            dist[p][k] = 0
        elif g[p][k] == 'F':
            f.append((p,k))

d = [(1,0),(-1,0),(0,1),(0,-1)]

while j:
    for _ in range(len(f)):
        fr,fc = f.popleft()
        for dfr,dfc in d:
            nfr,nfc = fr+dfr,fc+dfc
            if 0<=nfr<n and 0<=nfc<m and g[nfr][nfc] == '.':
                g[nfr][nfc] = 'F'
                f.append((nfr,nfc))
    
    for _ in range(len(j)):
        jr,jc = j.popleft()
        for djr,djc in d:
            njr,njc = jr+djr,jc+djc
            if 0> njr or n <= njr or 0> njc or m <= njc:
                print(dist[jr][jc] + 1)
                exit(0)
            if 0<=njr<n and 0<=njc<m:
                if g[njr][njc] == '.' and dist[njr][njc] == -1:
                    dist[njr][njc] = dist[jr][jc] + 1
                    j.append((njr,njc))

print("IMPOSSIBLE")