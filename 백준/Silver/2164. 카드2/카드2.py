import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(range(1,n+1))
while True:
    k = q.popleft()
    if q:
        q.append(q.popleft())
    else:
        break
print(k)