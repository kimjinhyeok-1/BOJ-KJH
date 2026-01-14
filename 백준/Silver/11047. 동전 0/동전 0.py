import sys
input = sys.stdin.readline

n, k = map(int, input().split())
tp = []
for _ in range(n):
    tp.append(int(input()))
tp1 = tp[::-1]

ans = 0
for t in tp1:
    if k>= t:
        ans += k//t
        k = k%t

print(ans)