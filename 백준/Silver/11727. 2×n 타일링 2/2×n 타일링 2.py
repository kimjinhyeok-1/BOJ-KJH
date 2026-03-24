import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
MOD = 10007

dp = [0] * (n+1)

if n == 1:
    print(1)
    sys.exit(0)
if n == 2:
    print(3)
    sys.exit(0)

dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = (dp[i-2] * 2 + dp[i-1]) % MOD

print(dp[n])