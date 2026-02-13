import sys
import heapq
input = sys.stdin.readline
n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
gems.sort()
bags.sort()

idx = 0
heap = []
total = 0

for x in bags:
    while idx < n and gems[idx][0] <= x:
        heapq.heappush(heap, -gems[idx][1])
        idx += 1
    if heap:
        total += (-heapq.heappop(heap))
print(total)