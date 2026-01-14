import sys
input = sys.stdin.readline
n = int(input())
kilo = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
min_price = price[0]

for i in range(n-1):
    if price[i] < min_price:
        min_price = price[i]
    result += min_price * kilo[i]

print(result)