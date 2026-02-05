import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    tk = input().strip()
    count = 0
    out = []
    for k in tk:
        if k == "O":
            count += 1
            out.append(count)
        elif k == "X":
            count = 0
            out.append(count)
    print(sum(out))