import sys
from collections import defaultdict
input = sys.stdin.readline
INF = 10**18
n,s = map(int, input().split())
nums = list(map(int, input().split()))
l = 0
sum = 0
ans = INF
for r in range(n):
    sum += nums[r]
    while sum >= s:
        ans = min(ans, r-l+1)
        sum -= nums[l]
        l+=1

if ans == INF: print(0)
else: print(ans)