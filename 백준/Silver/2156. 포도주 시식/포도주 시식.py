import sys
input = sys.stdin.readline

n = int(input())
grape = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(grape[1])
    sys.exit()
dp = [0] * (n+1)
dp[1] = grape[1]
dp[2] = grape[1] + grape[2]

for i in range(3, n+1):
    dp[i] = max(
        dp[i-1],
        dp[i-3] + grape[i-1] + grape[i],
        dp[i-2] + grape[i]
    )

print(dp[n])