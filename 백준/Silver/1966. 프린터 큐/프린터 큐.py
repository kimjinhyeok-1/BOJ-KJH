import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    pri = list(map(int, input().split()))
    dq = deque()
    for i in range(N):
        dq.append((pri[i], i == M))
    count = 0
    while True:
        p, mine = dq.popleft()
        if dq and p < max(x for x, _ in dq):
            dq.append((p, mine))
        else:
            count += 1
            if mine:
                print(count)
                break