def can_cross(stones, k, x):
    broken = 0

    for stone in stones:
        if stone < x:
            broken += 1

            if broken >= k:
                return False
        else:
            broken = 0

    return True


def solution(stones, k):
    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        if can_cross(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1

    return right