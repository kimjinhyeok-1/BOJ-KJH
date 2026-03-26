import sys
input = sys.stdin.readline

arr1 = list(input().strip())
arr2 = list(input().strip())

n = len(arr1)
m = len(arr2)
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if arr1[i-1] == arr2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])

a = n
b = m
ans = []
while a > 0 and b > 0:
    if arr1[a-1] == arr2[b-1]:
        ans.append(arr1[a-1])
        a -= 1
        b -= 1
    else:
        if dp[a][b-1] > dp[a-1][b]:
            b -= 1
        else:
            a -= 1
ans.reverse()
print("".join(ans))