import sys
input = sys.stdin.readline

word = input().strip()
l = len(word)
ans = [[0] * (l+1) for _ in range(26)]
for i in range(1,l+1):
    for j in range(26):
        ans[j][i] = ans[j][i-1]
    ans[ord(word[i-1]) - ord('a')][i] += 1  



q = int(input())
for i in range(q):
    a, i, j = map(str, input().split())
    i = int(i)
    j = int(j)
    print(ans[ord(a) - ord('a')][j+1] - ans[ord(a) - ord('a')][i])