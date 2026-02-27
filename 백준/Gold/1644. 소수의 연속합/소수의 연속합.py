import sys
input = sys.stdin.readline
n = int(input())

def sieve(n):
    p = [True] * (n+1)
    p[0] = p[1]= False
    i = 2
    while i * i <= n:
        for j in range(i*i, n+1, i):
            if p[i]:
                p[j] = False
        i += 1
    arr = [i for i in range(2, n+1) if p[i]]
    return arr

pri = sieve(n)
cur = 0
cnt = 0
s = 0
e = 0
while True:
    if cur >= n:
        if cur == n: cnt+=1
        cur -= pri[s]
        s += 1
    else:
        if e == len(pri): break
        cur += pri[e]
        e += 1
print(cnt)