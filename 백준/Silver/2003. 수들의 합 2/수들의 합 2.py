import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int, input().split()))
# 10 5
# 1 2 3 4 2 5 3 1 1 2

ans = 0
cur = 0
s = 0
e = 0
while s<n:
    if cur >= m:
        if cur == m: ans += 1
        cur -= num[s]
        s+= 1
    else:
        if e == n: break
        cur += num[e]
        e += 1

print(ans)