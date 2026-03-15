import sys
import heapq
input = sys.stdin.readline
arr = [list(map(int, input().split())) for _ in range(9)]
ans = 0
i = j = 0
for r in range(9):
    for c in range(9):
        if arr[r][c] > ans:
            i = r
            j = c
            ans = arr[r][c]
print(ans)
print(i+1, j+1)