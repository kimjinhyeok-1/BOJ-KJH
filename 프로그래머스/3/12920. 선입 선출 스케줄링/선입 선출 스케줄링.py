"""
우와 무지 어렵다!
생각해야 되는게 크게 두 가지
1. 몇초에 n개의 작업이 시작하는지 (Ex 2초에 6개의 작업이 시작, 처리 x)
2. 몇초를 구했으면 실제로 n번째 작업은 어떤 코어가 맡는지 -> 이게 극악
"""

def solution(n, cores):
    if n <= len(cores):
        return n

    left = 1
    right = max(cores) * n

    while left < right:
        mid = (left + right) // 2

        count = len(cores)
        for c in cores:
            count += mid // c

        if count >= n:
            right = mid
        else:
            left = mid + 1

    time = left

    count = len(cores)
    for c in cores:
        count += (time - 1) // c

    for i, c in enumerate(cores):
        if time % c == 0:
            count += 1

            if count == n:
                return i + 1