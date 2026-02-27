import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

ans = [0] * N
stack = []
for i in range(N-1,-1,-1):
    while stack and num[stack[-1]] <= num[i]:
        ans[stack.pop()] = i + 1

    stack.append(i)
print(" ".join(map(str, ans)))