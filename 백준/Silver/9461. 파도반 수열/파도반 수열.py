import sys 
input = sys.stdin.readline
T = int(input())
narr = []
max_n = 0
for _ in range(T):
    n = int(input())
    narr.append(n)
    max_n = max(max_n, n)

dp = [0] * (max_n + 1)
if max_n == 1:
   print(1)
   sys.exit(0) 
if max_n == 2:
   print(1)
   sys.exit(0) 
if max_n == 3:
   print(1)
   sys.exit(0) 
if max_n == 4:
   print(2)
   sys.exit(0) 
if max_n == 5:
   print(2)
   sys.exit(0) 
dp[1] = 1
dp[2] = 1 
dp[3] = 1
dp[4] = 2
dp[5] = 2
for n in range(6, max_n + 1):
    dp[n] = dp[n-1] + dp[n-5]
for n in narr:
    print(dp[n])