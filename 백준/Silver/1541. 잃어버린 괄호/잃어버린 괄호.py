n = input().split("-")
result = sum(map(int, n[0].split("+")))

for part in n[1:]:
    result -= sum(map(int, part.split("+")))

print(result)