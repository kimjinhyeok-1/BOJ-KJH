import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

count = {}
for x in card:
    count[x] = count.get(x, 0) + 1
out = []

for x in find:
    out.append(str(count.get(x, 0)))

print(" ".join(out))