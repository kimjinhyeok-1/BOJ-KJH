import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n + 1)
prev = [0] * (n + 1)

for i in range(2, n + 1):
    # 기본: 1 빼기
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    # 2로 나누기
    if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2

    # 3으로 나누기
    if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

print(dp[n])

path = []
cur = n
while cur != 0:
    path.append(cur)
    if cur == 1:
        break
    cur = prev[cur]

print(*path)