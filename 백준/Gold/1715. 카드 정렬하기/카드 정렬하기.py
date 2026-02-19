import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

ans = 0
if n == 1: 
    print(0)
    sys.exit()
for _ in range(n-1):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a + b
    ans += c
    heapq.heappush(heap, c)
print(ans)