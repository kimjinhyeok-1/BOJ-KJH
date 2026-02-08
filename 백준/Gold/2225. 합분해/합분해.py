import sys
input = sys.stdin.readline
mod = 1_000_000_000
n,k = map(int, input().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, k+1):
    dp[0][i] = 1
for j in range(1, n+1):
    dp[j][1] = 1
for kk in range(2, k+1):
    for p in range(1, n+1):
        dp[p][kk] = (dp[p-1][kk] + dp[p][kk-1]) % mod
print(dp[n][k])