import sys
from collections import defaultdict
input = sys.stdin.readline
n,k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = defaultdict(int)
cnt[0] = 1
ans = 0
cur = 0
for num in nums:
    cur  += num
    ans += cnt[cur - k]
    cnt[cur] += 1
print(ans)