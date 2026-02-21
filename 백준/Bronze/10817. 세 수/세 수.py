import sys
input = sys.stdin.readline
s = list(map(int, input().split()))
s.sort()
print(s[1])