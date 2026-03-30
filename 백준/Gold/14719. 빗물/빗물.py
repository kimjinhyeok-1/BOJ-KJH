import sys

h,w = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for i in range(w):
    left_max = max(arr[:i+1])
    right_max = max(arr[i:])
    ans += min(left_max, right_max) - arr[i]

print(ans)