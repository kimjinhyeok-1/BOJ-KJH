import sys
input = sys.stdin.readline

n,m = map(int, input().split())
list_d = {input().strip() for _ in range(n)}
list_b = []

for _ in range(m):
    name = input().strip()
    if name in list_d:
        list_b.append(name)

list_b.sort()
print(len(list_b))
print("\n".join(list_b))