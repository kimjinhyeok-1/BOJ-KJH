import sys 
input = sys.stdin.readline
n = int(input())
prices = list(map(int, input().split()))
dp = [0] * (n+1)
for i in range(0, n):
    for j in range(i+1, n+1):
        dp[j] = max(dp[j], dp[j-i-1] + prices[i] * 1)
print(dp[n])