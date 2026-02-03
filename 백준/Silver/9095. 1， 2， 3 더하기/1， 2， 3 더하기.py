import sys
input = sys.stdin.readline

t = int(input())
max_n = 0
ans = []
for _ in range(t):
    n = int(input())
    ans.append((n))
    max_n = max(max_n, n)

dp = [0] * 11
dp[1], dp[2], dp[3] = 1,2,4

for x in range(4,max_n + 1):
    dp[x] = dp[x-1] + dp[x-2] + dp[x-3]

for i in range(t):
    print(dp[ans[i]])