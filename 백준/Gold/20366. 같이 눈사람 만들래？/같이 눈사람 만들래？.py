import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

answer = float('inf')

for i in range(n - 3):
    for j in range(i + 3, n):
        target = arr[i] + arr[j]

        left = i + 1
        right = j - 1

        while left < right:
            snowman = arr[left] + arr[right]
            diff = abs(target - snowman)

            answer = min(answer, diff)
            if answer == 0:
                print(0)
                sys.exit(0)

            if snowman < target:
                left += 1
            else:
                right -= 1

print(answer)