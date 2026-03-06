import sys
input  = sys.stdin.readline

n = int(input())
cow = []
for _ in range(n):
    a,b = map(int, input().split())
    cow.append((a,b))

cow.sort()

s = e = 0
for ar, t in cow:
    if ar >= e:
        s = ar
        e = ar+ t
    elif ar< e:
        s = e
        e += t
print(e)