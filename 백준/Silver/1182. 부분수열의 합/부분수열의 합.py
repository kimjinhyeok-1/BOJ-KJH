import sys
input  = sys.stdin.readline

n,s = map(int, input().split())
arr =  list(map(int, input().split()))
ans = [0]
def dfs(idx, target):
    if idx == n:
        if target == s:
            ans[0] += 1
        return
    dfs(idx+1, target + arr[idx])
    dfs(idx+1, target)

dfs(0,0)
if s ==0: ans[0] -= 1
print(ans[0])