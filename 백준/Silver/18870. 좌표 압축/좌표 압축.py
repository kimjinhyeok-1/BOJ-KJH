import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

uniq = sorted(set(lst))

mp = {v:i for i, v in enumerate(uniq)}

out = [str(mp[x]) for x in lst]

print(" ".join(out))