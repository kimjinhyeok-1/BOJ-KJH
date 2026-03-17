import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M:
    broken = set(input().split())
else:
    broken = set()

ans = abs(N - 100)

for x in range(1000000):
    sx = str(x)
    cm= True

    for k in sx:
        if k in broken:
            cm = False
            break
    
    if cm:
        cost = len(sx) + abs(x - N)
        ans = min(ans, cost)
print(ans)