import sys
input = sys.stdin.readline
write = sys.stdout.write

n,m = map(int, input().split())
num = list(map(int, input().split()))
prefix = [0] *(n+1)
out = []
for i in range(1,n+1):
    prefix[i] = prefix[i-1] + num[i-1]

for _ in range(m):
    i,j = map(int, input().split())
    out.append(str(prefix[j] - prefix[i-1]))

write("\n".join(out))