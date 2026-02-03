import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 0
for x in range(2,n+1):
    dp[x] = dp[x-1] + 1
    if x%2 == 0:
        dp[x] = min(dp[x], dp[x//2] + 1)
    if x%3 == 0:
        dp[x] = min(dp[x], dp[x//3] + 1)
print(dp[n])