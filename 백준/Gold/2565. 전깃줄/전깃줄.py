import sys
input = sys.stdin.readline

n = int(input())
el = []
for _ in range(n):
    a,b = map(int, input().split())
    el.append((a,b))
el.sort()
b = []
for i in range(n):
    b.append(el[i][1])
dp = [1] * n
for i in range (n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[i], dp[j]+1)
ans = n - max(dp)
print(ans) 