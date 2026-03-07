import sys
input = sys.stdin.readline

n = int(input())

s = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+2)
for i in range(1, n+1):
    # 안 하는 경우
    dp[i+1] = max(dp[i+1], dp[i])

    # 하는 경우
    end = i + s[i][0]
    if end <= n+1:
        dp[end] = max(dp[end], dp[i] + s[i][1])

print(max(dp))