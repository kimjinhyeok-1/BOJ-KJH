import sys
input = sys.stdin.readline
MOD = 15746
n = int(input())

if n == 1: 
    print(1)
    sys.exit(0)
if n == 2: 
    print(2)
    sys.exit(0)

a,b = 1,2

for _ in range(3,n+1):
    a,b = b, (a+b) % MOD

print(b % MOD)