# 현재 퍼즐 난이도: diff
# 현재 퍼즐 소요시간: time_curr
# 이전 퍼즐의 소요시간: time_prev
# 숙련도: level

def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = max(diffs)
    while left <= right:
        level = (left + right) // 2
        
        total = 0
        if diffs[0] > level:
            total = (diffs[0] - level) * times[0] + times[0]
        else:
            total = times[0]
        for i in range(1, len(times)):
            if diffs[i] > level:
                total += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
            else:
                total += times[i]
        if total <= limit:
            answer = level
            right = level - 1
        else:
            left = level + 1
    return answer