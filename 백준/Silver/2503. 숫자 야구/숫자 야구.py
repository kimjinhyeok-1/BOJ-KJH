import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())

hints = []
answer = 0
for _ in range(N):
    num, s, b = input().split()
    hints.append((num, int(s), int(b)))

for x in permutations('123456789', 3):
    k = ''.join(x)
    p = True

    for num, s, b in hints:
        strike = 0
        ball = 0
        for i in range(3):
            if num[i] == k[i]:
                strike += 1
            elif num[i] in k:
                ball += 1
        if strike != s or ball != b:
            p = False
            break
    if p:
        answer += 1
print(answer)