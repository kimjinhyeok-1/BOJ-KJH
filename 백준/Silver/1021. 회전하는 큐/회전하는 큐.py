import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lst= list(map(int, input().split()))
q = deque(range(1, N+1))
count = 0 
for x in lst:
    idx = q.index(x)
    left = idx
    right = len(q) - idx
    if left <= right:
        q.rotate(-left)
        count += left
    else:
        q.rotate(right)
        count += right
    
    q.popleft()

print(count)