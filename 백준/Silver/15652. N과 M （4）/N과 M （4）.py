import sys
input = sys.stdin.readline

n,m = map(int, input().split())

arr = []

def dfs(depth, start):
    if depth == m:
        print(*arr)
        return
    for i in range(start, n+1):
        arr.append(i)
        dfs(depth+1, i)
        arr.pop()

dfs(0,1)