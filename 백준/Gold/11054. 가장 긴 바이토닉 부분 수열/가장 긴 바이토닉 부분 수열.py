import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lis = [1] * n
lst_r = list(reversed(lst))
lds = [1] * n
for i in range(1, n):
    for j in range(i):
        if lst[i]>lst[j]:
            lis[i] = max(lis[i], lis[j] + 1)
for k in range(1, n):
    for p in range(k):
        if lst_r[k]>lst_r[p]:
            lds[k] = max(lds[k], lds[p] + 1)
lds.reverse()
ans = 0
for i in range(n):
    ans = max(ans, lds[i] + lis[i])
print(ans-1)