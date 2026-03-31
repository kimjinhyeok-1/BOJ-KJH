import sys
from collections import Counter
input = sys.stdin.readline

s = input().strip()
count = Counter(s)

count_p = 0
mid = ''
for ch, c in count.items():
    if c % 2 == 1:
        mid = ch
        count_p += 1

if count_p > 1:
    print('I\'m Sorry Hansoo')
    sys.exit()

left = []
for ch in sorted(count):
    for _ in range(count[ch] // 2):
        left.append(ch)

left = "".join(left)
right = "".join(reversed(left))
ans = left + mid + right

print(ans)