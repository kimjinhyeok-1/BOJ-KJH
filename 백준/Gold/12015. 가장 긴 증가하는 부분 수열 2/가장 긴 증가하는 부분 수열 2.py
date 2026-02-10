import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
out = []
for x in nums:
    if len(out) == 0 or x > out[-1]:
        out.append(x)
    else:
        idx = bisect_left(out, x)
        out[idx] = x
print(len(out))