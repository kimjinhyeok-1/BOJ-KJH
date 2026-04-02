import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def check(l,r):
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

for _ in range(n):
    s = input().strip()
    l = 0
    r = len(s) - 1
    
    while l < r and s[l] == s[r]:
        l += 1
        r -= 1
    if l >= r:
        print(0)
    elif check(l+1,r) or check(l, r-1):
        print(1)
    else:
        print(2)