import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dict = defaultdict(int)
    for _ in range(n):
        a, b = input().split()
        dict[b] += 1
    ans = 1
    for p in dict:
        ans *= (dict[p] + 1)
    print(ans - 1)