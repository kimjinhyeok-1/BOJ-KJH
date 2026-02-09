import sys
input = sys.stdin.readline

word = input().strip()
q = int(input())
for i in range(q):
    a, i, j = map(str, input().split())
    count = 0
    for k in range(int(i), int(j)+1):
        if word[k] == a:
            count += 1
    print(count)