import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    counts = {}
    for _ in range(n):
        name, kind = input().split()
        counts[kind] = counts.get(kind, 0) + 1
    ans = 1
    for kind in counts:
        ans *= counts[kind] + 1
    print(ans - 1)
