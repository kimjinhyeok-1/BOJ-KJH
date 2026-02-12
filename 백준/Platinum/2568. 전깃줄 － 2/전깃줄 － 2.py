import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
el = [list(map(int, input().split())) for _ in range(n)]
el.sort()  # A 기준 정렬

el2 = [b for a, b in el]  # B만

result = []          # tails (최소 끝값)
last_idx = []        # 각 길이별 마지막 원소의 인덱스
parent = [-1] * n    # 역추적 포인터

for i in range(n):
    x = el2[i]
    k = bisect_left(result, x)

    if k == len(result):
        result.append(x)
        last_idx.append(i)
    else:
        result[k] = x
        last_idx[k] = i

    if k > 0:
        parent[i] = last_idx[k - 1]

L = len(result)

keep = [False] * n
idx = last_idx[L - 1]
while idx != -1:
    keep[idx] = True
    idx = parent[idx]

removeA = []
for i in range(n):
    if not keep[i]:
        removeA.append(el[i][0])

print(len(removeA))
for a in removeA:
    print(a)
