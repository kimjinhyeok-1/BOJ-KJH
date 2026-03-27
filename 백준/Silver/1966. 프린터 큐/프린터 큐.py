'''
우리가 원하는 것: 몇번째로 출력이 되는지
출력되는 조건: 프린트 했을 때 우리가 원하는 것 출력되면 
while True:
---- 특정 조건 -----
break
'''
import sys
from collections import deque



T = int(input())
for _ in range(T):
    q = deque()
    count = 0
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    for i in range(n):
        q.append((i, imp[i]))
    while True:
        idx, cur = q.popleft()
        if any(cur < x[1] for x in q):
            q.append((idx,cur))
        else:
            count += 1
            if idx == m:
                print(count)
                break