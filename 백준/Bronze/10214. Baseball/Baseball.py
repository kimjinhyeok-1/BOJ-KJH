import sys
input  = sys.stdin.readline

T = int(input())
ans = []
for _ in range(T):
    
    y = 0
    k = 0
    for _ in range(9):
        a, b = map(int, input().split())
        y += a
        k += b
    if y > k:
        ans.append("Yonsei")
    elif y < k:
        ans.append("Korea")
    else:
        ans.append("Draw")
print("\n".join(ans))