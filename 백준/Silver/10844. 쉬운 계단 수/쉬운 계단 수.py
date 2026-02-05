import sys
input = sys.stdin.readline
mod = 1000000000
n = int(input())

dp = [[0] * 10 for _ in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1

for k in range(2, n+1):
    for p in range(0, 10):
        if p == 0:
            dp[k][p] += dp[k-1][p+1]
        elif p == 9:
            dp[k][p] += dp[k-1][p-1]
        else:
            dp[k][p] = dp[k-1][p-1] + dp[k-1][p+1]

ans = 0
for i in range(0,10):
    ans += dp[n][i]
print(ans%mod)