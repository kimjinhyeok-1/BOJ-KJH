import sys
input = sys.stdin.readline

n, B, C = map(int, input().split())
a = list(map(int, input().split()))
a += [0, 0]  # 경계 처리

# B <= C 이면 묶음 이득이 없으므로 무조건 1개씩 사는 게 최적
if B <= C:
    print(sum(a[:n]) * B)
    sys.exit()

ans = 0

for i in range(n):
    # 2번 공장 수량이 3번 공장보다 많으면 (i,i+1) 2개 묶음을 먼저 처리
    if a[i+1] > a[i+2]:
        x = min(a[i], a[i+1] - a[i+2])
        ans += x * (B + C)
        a[i] -= x
        a[i+1] -= x

    # (i,i+1,i+2) 3개 묶음 최대한 처리
    y = min(a[i], a[i+1], a[i+2])
    ans += y * (B + 2*C)
    a[i] -= y
    a[i+1] -= y
    a[i+2] -= y

    # (i,i+1) 2개 묶음 처리
    z = min(a[i], a[i+1])
    ans += z * (B + C)
    a[i] -= z
    a[i+1] -= z

    # 남은 건 1개씩
    ans += a[i] * B
    a[i] = 0

print(ans)
