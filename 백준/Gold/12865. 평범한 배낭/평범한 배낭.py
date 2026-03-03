import sys
input = sys.stdin.readline

n, k = map(int, input().split())
bag = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]


dp = [[0] * (k+1) for _ in range(n+1)]
for i in range(1,n+1):
    wi ,vi = bag[i]
    for w in range(k+1):
        dp[i][w] = dp[i-1][w]
        if w >= wi:
            dp[i][w] = max(dp[i][w], dp[i-1][w-wi] + vi)
print(dp[n][k]) 