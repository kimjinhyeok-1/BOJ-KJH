import sys
input = sys.stdin.readline

n = int(input())
r, g, b = map(int, input().split())
prev = [r, g, b]

for _ in range(n - 1):
    r, g, b = map(int, input().split())
    cur = [
        r + min(prev[1], prev[2]),
        g + min(prev[0], prev[2]),
        b + min(prev[0], prev[1])
    ]
    prev = cur

print(min(prev))
