import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = {input().strip() for _ in range(n)}

count = 0

for _ in range(m):
    if input().strip() in s:
        count += 1
        

print(count)
