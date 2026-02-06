import sys
input = sys.stdin.readline
INF = 10**18
n = int(input())

# gr = [0] + [int(input()) for _ in range(n)]
# dp = [[0,0,0] for _ in range(n+1)]
# dp[0][0] = 0
# dp[0][1] = -INF
# dp[0][2] = -INF
# for i in range(1, n+1):
#     dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2] )
#     dp[i][1] = dp[i-1][0] + gr[i]
#     dp[i][2] = dp[i-1][1] + gr[i]
# print(max(dp[n]))

ans =  [0, -INF, -INF]
for _ in range(n):
    w = int(input())
    gr = [
        max(ans[0], ans[1], ans[2]),
        ans[0] + w,
        ans[1] + w
    ]
    ans = gr
print(max(ans))