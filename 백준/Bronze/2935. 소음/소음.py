import sys
input = sys.stdin.readline

a = int(input())
s = input().strip()
b = int(input())

if s == '+':
    print(a + b)
   
else:
    print(a * b)