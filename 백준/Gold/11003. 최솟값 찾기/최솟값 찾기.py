import sys
from collections import deque
input = sys.stdin.readline
dq = deque()
N, L = map(int, input().split())
num = list(map(int, input().split()))
out = []

for i, x in enumerate(num):
    while dq and dq[-1][0] >= x:
        dq.pop()
    dq.append((x, i))
    if dq and dq[0][1] <= i - L:
        dq.popleft()
    out.append(str(dq[0][0]))

print(" ".join(out))