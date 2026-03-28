import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dp = [0] * n
dp[0] = int(input())

for i in range(1, n):
    nums = list(map(int, input().split()))
    for j in range(i, -1, -1):
        if j == 0:
            dp[0] += nums[0]
        elif j == i:
            dp[j] = dp[j-1] + nums[j]
        else:
            dp[j] = nums[j] + max(dp[j], dp[j-1])
print(max(dp))