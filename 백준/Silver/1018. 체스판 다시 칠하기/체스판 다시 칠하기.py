import sys 
input = sys.stdin.readline
INF = 10**18

n,m = map(int, input().split())
ch = [input().strip() for _ in range(n)]

col = 'W'
ans = INF
for i in range(n-7):
    for j in range(m-7):
        t = 0
        for x in range(8):
            for y in range(8):
                if (x+y) % 2 == 0 and col != ch[i+x][j+y]:
                    t += 1
                elif (x+y) % 2 == 1 and col == ch[i+x][j+y]:
                    t += 1
        t = min(t, 64-t)
        ans = min(t, ans)
print(ans)