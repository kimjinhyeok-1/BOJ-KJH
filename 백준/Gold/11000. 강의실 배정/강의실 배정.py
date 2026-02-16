import sys 
import heapq
input = sys.stdin.readline
n = int(input())
lt = [list(map(int, input().split())) for _ in range(n)]
lt.sort()
heap =[]

for s, e in lt:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
print(len(heap))