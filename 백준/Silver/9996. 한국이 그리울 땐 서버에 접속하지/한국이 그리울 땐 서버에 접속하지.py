import sys
input = sys.stdin.readline

n = int(input())
a, b = input().strip().split("*")
la = len(a)
lb = len(b)
ls = la+lb

for _ in range(n):
    s = input().strip()
    if a == s[:la] and b == s[len(s) - lb:] and len(s) >= ls:
        print("DA")
    else:
        print("NE")