import sys
input = sys.stdin.readline
T = int(input())
ans = 0

for _ in range(T):
    word = input().strip()
    seen=[]
    prev = word[0]
    seen.append(prev)
    is_group = True
    for i in range(1, len(word)):
        cur = word[i]
        if cur == prev:
            continue
        else:
            if cur in seen:
                is_group = False
                break
            else:
                seen.append(cur)
                prev = cur

    if is_group == True:
        ans += 1

print(ans)        