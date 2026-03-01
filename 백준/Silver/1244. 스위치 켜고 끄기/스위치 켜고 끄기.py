import sys
input = sys.stdin.readline

n = int(input())
ans = list(map(int, input().split()))
s_n = int(input())

def ch_n(x):
    return 1 - x

for _ in range(s_n):
    g, k = map(int, input().split())
    if g == 1:
        for x in range(k-1, n, k):
            ans[x] = ch_n(ans[x])
    else:
        ans[k-1] = ch_n(ans[k-1])
        for i in range(1, n):
            if k-1-i < 0 or k-1+i > n-1:
                break
            if ans[k-1-i] == ans[k-1+i]:
                ans[k-1-i] = ch_n(ans[k-1-i])
                ans[k-1+i] = ch_n(ans[k-1+i])
            else:
                break

for i in range(0, n, 20):
    print(*ans[i:i+20])