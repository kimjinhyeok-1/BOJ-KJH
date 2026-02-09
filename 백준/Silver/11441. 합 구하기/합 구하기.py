import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
prefix = [0] * (n+1)
ans = []

for i in range(1,n+1):
    prefix[i] = prefix[i-1] + num[i-1]

for _ in range(m):
    i,j = map(int,input().split())
    a = prefix[j] - prefix[i-1]
    ans.append(str(a))

print("\n".join(ans))