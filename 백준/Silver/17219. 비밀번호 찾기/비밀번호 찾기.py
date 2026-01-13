import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
out = []

for _ in range(n):
    i, v= input().split()
    d[i] = v

for _ in range(m):
    site = input().strip()
    out.append(d[site])

print("\n".join(out))