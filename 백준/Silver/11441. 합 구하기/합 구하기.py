import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
m = int(input())
ans = 0
for _ in range(m):
    i,j = map(int, input().split())
    ans = sum(num[i-1:j])
    print(ans)