import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

no_hear = {input().strip() for _ in range(n)}
no_see = {input().strip() for _ in range(m)}

ans = sorted(no_hear & no_see)
print(len(ans))
print("\n".join(ans))