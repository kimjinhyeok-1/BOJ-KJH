import sys
from bisect import bisect_left
input = sys.stdin.readline
INF = 10**18
n = int(input())
nums = list(map(int, input().split()))
out = []
dp = []
for x in nums:
    if len(out) == 0 or out[-1] < x:
        out.append(x)
        k = len(out) - 1
        dp.append([x,k])
    else:
        idx = bisect_left(out, x)
        out[idx] = x
        dp.append([x,idx])
l = len(out)
dp.reverse()

result = []
i = l-1
for j in range(len(dp)):
    if dp[j][1] == i:
        result.append(dp[j][0])
      
        i -= 1
print(l)
result.reverse()
print(" ".join(map(str, result)))