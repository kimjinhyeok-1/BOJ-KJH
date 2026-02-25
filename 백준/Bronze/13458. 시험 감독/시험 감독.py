import sys
input = sys.stdin.readline

n = int(input())
num = map(int, input().split())
b,c = map(int, input().split())

cnt = 0

for x in num:
    cnt += 1
    if x > b:
        cnt += (x - b + c -1 ) // c
print(cnt)