import sys
from collections import deque
input = sys.stdin.readline

def d(n):
    return n + sum(map(int, str(n)))

generated = [False] * 10001

for i in range(1, 10001):
    num = d(i)
    if num <= 10000:
        generated[num] = True

for i in range(1, 10001):
    if not generated[i]:
        print(i)