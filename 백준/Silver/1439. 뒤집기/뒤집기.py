import sys
input = sys.stdin.readline

nums = list(map(int, input().strip()))

zc = 0
oc = 0

if nums[0] == 0:
    zc += 1
elif nums[0] == 1:
    oc += 1

prev = nums[0]
for curr in nums[1:]:
    if prev != curr:
        if curr == 0:
            zc += 1
        elif curr == 1:
            oc += 1
    prev = curr

print(min(zc,oc))