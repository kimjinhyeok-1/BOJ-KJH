import sys
input = sys.stdin.readline
n = int(input())
lst = []
out = []
for _ in range(n):
    parts = input().strip().split()
    cmd = parts[0]
    if cmd == "push":
        lst.append(parts[1])
    elif cmd == "pop":
        if len(lst) == 0:
            out.append("-1")
        elif len(lst) != 0:
            out.append(lst.pop())
    elif cmd == "size":
        out.append(str(len(lst)))
    elif cmd == "empty":
        if len(lst) == 0:
            out.append("1")
        elif len(lst) != 0:
            out.append("0")
    elif cmd == "top":
        if len(lst) == 0:
            out.append("-1")
        else:
            out.append(lst[-1])

print("\n".join(out))