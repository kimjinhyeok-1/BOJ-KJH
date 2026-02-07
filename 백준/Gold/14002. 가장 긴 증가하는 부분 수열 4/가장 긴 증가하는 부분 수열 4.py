import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp =  [1] * n
parent = [-1] * n
for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
print(max(dp))
idx = dp.index(max(dp))
ans = []
for i in range(max(dp)):
    ans.append(lst[idx])
    idx = parent[idx]
ans.reverse()
print(" ".join(map(str,ans)))