import sys
input = sys.stdin.readline
MOD = 10007
n = int(input())
dp = [0] * (n+1)
if n == 1:
    print(1)
    sys.exit(0)
if n == 2:
    print(2)
    sys.exit(0)
dp[1], dp[2] = 1,2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % MOD)