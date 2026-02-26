import sys 
input = sys.stdin.readline

n,x = map(int, input().split())
tem = list(map(int,input().split()))
cur = sum(tem[:x])
mx = cur
for i in range(x,n):
    cur += tem[i] - tem[i-x]
    mx = max(mx, cur)
print(mx)