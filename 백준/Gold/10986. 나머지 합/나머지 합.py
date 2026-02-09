import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int,input().split()))
p = [0] * n
p[0] = num[0]
for i in range(1,n):
    p[i] = p[i-1] + num[i]
k = [0] * m
for x in p:
    k[x%m] += 1
ans = 0

k[0] += 1
for y in k:
    ans += (y*(y-1))//2

print(ans)