import sys
input = sys.stdin.readline

n = int(input())
ans = [[int(input())]]
for i in range(1, n):
    k = list(map(int, input().split()))
    for j in range(i+1):
        if j == 0:
            k[j] = ans[i-1][j] + k[j]
        elif j == i:
            k[j] = ans[i-1][j-1] + k[j]
        else:
            k[j] = k[j] + max(ans[i-1][j-1], ans[i-1][j])
    ans.append(k)
print(max(ans[-1]))