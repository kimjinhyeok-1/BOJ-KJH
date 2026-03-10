import sys
input = sys.stdin.readline
r,c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]
b = [list(map(int, input().split())) for _ in range(r)]
ans = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        ans[i][j] = a[i][j] + b[i][j]

for k in range(r):
    print(*ans[k], end = "\n")
