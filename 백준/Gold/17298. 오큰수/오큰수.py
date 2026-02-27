import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

stack = []
ans = [-1] * N
for i in range(N):
    while stack and num[stack[-1]] < num[i]:
        ans[stack.pop()] = num[i]
    stack.append(i)

print(" ".join(map(str, ans)))