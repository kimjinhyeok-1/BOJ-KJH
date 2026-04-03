import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def D(n):
    return (2 * n) % 10000

def S(n):
    if n == 0:
        return 9999
    return n - 1

def L(n):
    return (n % 1000) * 10 + (n // 1000)

def R(n):
    return (n % 10) * 1000 + (n // 10)

for _ in range(T):
    a, b = map(int, input().split())

    visited = [""] * 10000
    q = deque([a])
    visited[a] = "-"   # 시작점 표시용

    while q:
        cur = q.popleft()

        if cur == b:
            print(visited[cur][1:])
            break

        for nxt, op in ((D(cur), 'D'), (S(cur), 'S'), (L(cur), 'L'), (R(cur), 'R')):
            if visited[nxt] == "":
                visited[nxt] = visited[cur] + op
                q.append(nxt)