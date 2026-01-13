import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heard = {input().strip() for _ in range(n)}

ans = []

for _ in range(m):
    name = input().strip()
    if name in heard:
        ans.append(name)
        
ans.sort()
print(len(ans))
print("\n".join(ans))