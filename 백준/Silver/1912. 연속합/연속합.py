import sys
input = sys.stdin.readline
n = int(input())

arr = [0] + list(map(int, input().split()))
cur = arr[1]
best = arr[1]
for j in range(2, n+1):
    cur = max(arr[j], cur + arr[j])
    best = max(best, cur)  
print(best)