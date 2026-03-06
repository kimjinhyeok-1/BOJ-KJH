import sys
input  = sys.stdin.readline

s = input().strip()
ans = []
stack = []
is_tag = False
for a in s:
    if a == '<':
        print("".join(stack[::-1]), end = "")
        stack = []
        stack.append("<")
        is_tag = True
    elif a == '>':
        stack.append(">")
        print("".join(stack), end = "")
        stack = []
        is_tag = False
    elif a == " " and not is_tag:
        print("".join(stack[::-1]), end = "")
        print(" ", end = "")
        stack = []
    else:
        stack.append(a)
print("".join(stack[::-1]), end = "")