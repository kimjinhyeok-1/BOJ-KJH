import sys

input = sys.stdin.readline
INF = 10**9
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [INF] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i-coin] + 1, dp[i])

if dp[k] != INF:
    print(dp[k])
else:
    print(-1)