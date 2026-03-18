import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
MAX = 1000000
chik = []
houses = []
ans = MAX

for r in range(n):
    for c in range(n):
        if grid[r][c] == 1:
            houses.append((r,c))
        elif grid[r][c] == 2:
            chik.append((r,c))

for comb in combinations(chik, m):
    total = 0
    for hx,hy in houses:
        temp = MAX
        for cx, cy in comb:
            temp = min(temp, abs(hx-cx)+abs(hy-cy))
        total += temp
    ans = min(ans, total)
print(ans)