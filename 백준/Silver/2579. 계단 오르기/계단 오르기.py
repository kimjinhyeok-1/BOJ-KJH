import sys
input = sys.stdin.readline
n = int(input()) # n = 6
score = [int(input()) for _ in range(n)] # score = [10, 20, 15, 25, 10, 20]
dp = [[-1] * 2 for _ in range(n+1)] # dp = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

dp[1][0] = 0
dp[1][1] = score[0]

if (n == 1):
    print(max(dp[n][0], dp[n][1]))
    sys.exit(0)
dp[2][0] = score[0] + score[1]
dp[2][1] = score[1]
for i in range(3, n+1):
    dp[i][0] = dp[i-1][1] + score[i-1]
    dp[i][1] = max(dp[i-2][0], dp[i-2][1]) + score[i-1]

print(max(dp[n][0], dp[n][1]))