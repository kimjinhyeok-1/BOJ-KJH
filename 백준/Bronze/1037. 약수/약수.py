import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = lst[0] * lst[n-1]

print(ans)