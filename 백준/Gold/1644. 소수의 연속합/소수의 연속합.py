import sys
input = sys.stdin.readline
n = int(input())

def sieve(n):
    if n < 2:
        return []

    p = [True] * (n + 1)
    p[0] = p[1] = False

    i = 2
    while i * i <= n:
        if p[i]:  # i가 소수일 때만 배수 지우기
            for j in range(i * i, n + 1, i):
                p[j] = False
        i += 1

    return [x for x in range(2, n + 1) if p[x]]

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