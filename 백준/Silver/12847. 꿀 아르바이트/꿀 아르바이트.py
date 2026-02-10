import sys
from collections import defaultdict
input = sys.stdin.readline
n,m = map(int, input().split())
nums = list(map(int, input().split()))
cur = sum(nums[0:m])
ans = cur
for r in range(m, n):
    cur += nums[r]
    cur -= nums[r-m]
    ans = max(ans, cur)

print(ans)