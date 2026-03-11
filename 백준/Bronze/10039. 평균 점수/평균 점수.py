import sys
input = sys.stdin.readline

ans = 0
num = []
for _ in range(5):
    num.append(int(input()))
for n in num:
    if n < 40:
        n = 40
    ans += n
print(ans//5)