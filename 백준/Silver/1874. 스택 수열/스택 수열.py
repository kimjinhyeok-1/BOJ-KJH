import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
target = []
stack = []
out = []
cur = 1
possible = True

for _ in range(n):
    target.append(int(input()))

for x in target:
    while cur<= x:
        stack.append(cur)
        out.append("+")
        cur += 1
    if stack and stack[-1] == x:
        stack.pop()
        out.append("-")
    else:
        print("NO")
        possible = False
        break

if possible:
    print("\n".join(out))