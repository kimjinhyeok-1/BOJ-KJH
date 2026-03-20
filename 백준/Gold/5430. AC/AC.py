import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = input().strip()
    rev = False
    err = False

    if n == 0:
        q = deque()
    else:
        q = deque(arr[1:-1].split(','))

    for cmd in p:
        if cmd == 'R':
            rev = not rev
        elif cmd == 'D':
            if not q:
                err = True
                break
            if rev:
                q.pop()
            else:
                q.popleft()
    
    if err:
        print('error')
    else:
        if rev:
            q.reverse()
        print('[' + ",".join(q) + ']')