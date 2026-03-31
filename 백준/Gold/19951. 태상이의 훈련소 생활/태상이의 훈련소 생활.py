import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = list(map(int, input().split()))
diff = [0] * (n+1)

for _ in range(m):
    a,b,k = map(int,input().split())
    diff[a-1] += k
    diff[b] -= k

curr = 0
for i in range(n):
    curr += diff[i]
    arr[i] += curr

print(*arr)