import sys
input = sys.stdin.readline

n = int(input())
narry = set(map(int, input().split()))
m = int(input())
marry = map(int, input().split())

for k in marry:
    if k in narry:
        print(1)
    else:
        print(0)
