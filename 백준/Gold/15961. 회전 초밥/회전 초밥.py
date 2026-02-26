import sys
from collections import defaultdict
input = sys.stdin.readline

n,d,k,c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi = sushi + sushi
# 7, 9, 7, 30, 2, 7, 9, 25, 7, 9, 7, 30
dis = 0
count = defaultdict(int)
for i in range(k):
    count[sushi[i]] += 1
    if count[sushi[i]] == 1:
        dis += 1
score = dis + (1 if count[c] == 0 else 0)
ans = score

for x in range(k, n+k -1):
    out_sushi = sushi[x-k]
    count[out_sushi] -= 1
    if count[out_sushi] == 0:
        dis -= 1
    
    in_sushi = sushi[x]
    count[in_sushi] += 1
    if count[in_sushi] == 1:
        dis += 1

    score = dis + (1 if count[c] == 0 else 0)
    ans = max(ans, score)
print(ans)