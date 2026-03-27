import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
uniq = sorted(set(nums))

k = {v:i for i,v in enumerate(uniq)}

ans = []
for num in nums:
    ans.append(str(k[num]))

print(" ".join(ans))