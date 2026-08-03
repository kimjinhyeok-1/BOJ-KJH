def solution(s):
    answer = len(s)
    l = len(s)
    for unit in range(1, l // 2 + 1):
        result = ""
        prev = s[:unit]
        count = 1
        for i in range(unit, l, unit):
            curr = s[i:i + unit]
            if prev == curr:
                count += 1
            else:
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev
                count = 1
                prev = curr
        if count > 1:
            result += str(count) + prev
        else:
            result += prev
        answer = min(answer, len(result))
        
    return answer