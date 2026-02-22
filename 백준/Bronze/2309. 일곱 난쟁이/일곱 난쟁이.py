import sys 
input = sys.stdin.readline

lst = [int(input()) for _ in range(9)]

a = 0
b = 0
found = False
lst.sort()
total = sum(lst)
for i in range(9):
    for j in range(i+1,9):
        if total - lst[i] - lst[j] == 100:
            a = i
            b = j
            found = True

for k in range(9):
    if k != a and k != b and found:
        print(lst[k])