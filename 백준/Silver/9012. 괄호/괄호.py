import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = input().strip()
    count = 0
    ok = True
    for ch in s:
        if ch == "(":
            count += 1
        elif ch == ")":
            count -= 1
            if count < 0:
                ok = False
                break
    if ok and count == 0:
        print("YES")
    else:
        print("NO")