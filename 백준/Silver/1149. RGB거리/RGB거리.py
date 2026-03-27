import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

rgb = list(map(int, input().split()))
for _ in range(n-1):
    r,g,b = map(int, input().split())
    temp = [
        min(rgb[1] + r, rgb[2] + r),
        min(rgb[0] + g, rgb[2] + g),
        min(rgb[0] + b, rgb[1] + b)
    ]
    rgb = temp

print(min(rgb))