import sys
input = sys.stdin.readline

s = input().strip().split('-')
nums = [sum(map(int, x.split("+"))) for x in s]
ans = nums[0] - sum(nums[1:])
print(ans)