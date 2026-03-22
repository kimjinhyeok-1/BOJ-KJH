import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
a = [0] + [int(input()) for _ in range(N)]

INF = 10**18
dp = [INF] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    mn = mx = a[i]
    for j in range(i, max(0, i - M), -1):
        mn = min(mn, a[j])
        mx = max(mx, a[j])
        cost = K + (mx - mn) * (i - j + 1)
        dp[i] = min(dp[i], dp[j - 1] + cost)

print(dp[N])