import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))

ans = defaultdict(int)

for x in nums:
    ans[x] += 1

out = []

for x in s:
    out.append(str(ans[x]))
print(" ".join(out))