import sys 
input = sys.stdin.readline

s = input().strip()
count = [0] * 10
for x in s:
    if x == '9' and count[9] - count[6] == 1:
        count[6] += 1
    elif x == '6' and count[6] - count[9] == 1:
        count[9] += 1
    else:
        count[int(x)] += 1
print(max(count))