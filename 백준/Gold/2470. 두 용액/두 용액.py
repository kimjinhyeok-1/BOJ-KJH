import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
INF = 10**18
l = 0
r = N-1
best = INF
best_pair = [li[l], li[r]]
li.sort()
while l < r:
    s = li[l] + li[r]
    if best > abs(s):
        best = abs(s)
        best_pair = (li[l], li[r])
    if s > 0:
        r -= 1
    elif s < 0: 
        l += 1
    else:
        break
print(" ".join(map(str,best_pair)))