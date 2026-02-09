import sys
input = sys.stdin.readline
n,m = map(int, input().split())
num = list(map(int,input().split()))
p = [0] * m
p[0] = 1
count = 0
cur = 0
for x in num:
    cur = (cur + x) % m
    p[cur] += 1
for y in p:
    count += y * (y-1)//2
print(count)