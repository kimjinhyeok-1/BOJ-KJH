import sys
input = sys.stdin.readline

is_True = False
a,b = map(int, input().split())
cnt = 0
while a<=b:
    if b == a:
        is_True = True
        break
    if b % 2 == 0:
        b = b // 2
        cnt += 1
    elif b % 10 == 1:
        b = b // 10
        cnt += 1
    else:
        break

if is_True:
    print(cnt+1)
else: 
    print(-1)