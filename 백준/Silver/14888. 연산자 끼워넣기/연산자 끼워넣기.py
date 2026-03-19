import sys
from itertools import permutations
input = sys.stdin.readline
MAX = 1000000000
MIN = -MAX

n = int(input())
arr = list(map(int, input().split()))
plus, minus, time, divide = map(int,input().split())

ops = []
ops += ['+'] * plus
ops += ['-'] * minus
ops += ['*'] * time
ops += ['/'] * divide

cases = set(permutations(ops))

ma = MIN
mi = MAX
for case in cases:
    result = arr[0]
    for i in range(len(case)):
        if case[i] == '+':
            result += arr[i+1]
        elif case[i] == '-':
            result -= arr[i+1]
        elif case[i] == '*':
            result *= arr[i+1]
        elif case[i] == '/':
            if result < 0:
                result = -((-result) // arr[i+1])
            elif result>=0:
                result = result // arr[i+1]
    ma = max(ma,result)
    mi = min(mi,result)

print(ma)
print(mi)