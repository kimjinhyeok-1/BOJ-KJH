import sys
from itertools import permutations
input = sys.stdin.readline
MAX = 1000000000
MIN = -MAX
ma = MIN
mi = MAX
n = int(input())
arr = list(map(int, input().split()))
plus, minus, time, divide = map(int,input().split())

def dfs(idx, result, plus, minus, time, divide):
    global ma,mi
    if idx == n:
        ma = max(ma,result)
        mi = min(mi,result)
        return
    if plus>0:
        dfs(idx+1, result + arr[idx], plus -1, minus,time,divide)
    if minus>0:
        dfs(idx+1, result - arr[idx], plus, minus-1,time,divide)
    if time>0:
        dfs(idx+1, result * arr[idx], plus, minus,time-1,divide)
    if divide>0:
        if result<0:
            dfs(idx+1, -((-result) // arr[idx]), plus, minus,time,divide-1)
        else:
            dfs(idx+1, result // arr[idx], plus, minus, time, divide - 1)

dfs(1, arr[0], plus, minus, time, divide)

print(ma)
print(mi)