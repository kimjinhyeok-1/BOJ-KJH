import sys
from collections import deque
input = sys.stdin.readline
INF = 10**9
n = int(input())

prices = [0] + list(map(int, input().split()))
dp = [0] + [INF] * n

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = min(dp[i], dp[i-j] + prices[j])
print(dp[n])