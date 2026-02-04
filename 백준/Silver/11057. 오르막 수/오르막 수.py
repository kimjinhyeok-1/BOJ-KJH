import sys
input = sys.stdin.readline
n = int(input()) # n = 6
MOD = 10007

dp = [[0] * 10 for _ in range(n+1)]
for i in range(10):
    dp[1][i] = 1

for x in range(2,n+1):
    for y in range(10):
        if y==0:
            dp[x][y] = 1
        else:
            dp[x][y] = dp[x-1][y] + dp[x][y-1] #dp[x-1][0....y]
ans = 0
for i in range(10):
    ans += dp[n][i]
print(ans % MOD)