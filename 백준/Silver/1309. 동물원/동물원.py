import sys
input = sys.stdin.readline
mod = 9901
n = int(input())

dp = [1, 1, 1]
for _ in range(n-1):
    nxt = []
    nxt = [ 
        (sum(dp)) % mod,
        (sum([dp[0], dp[2]])) % mod,
        (sum([dp[0], dp[1]])) % mod
    ]
    dp = nxt
print((sum(dp)) % mod)