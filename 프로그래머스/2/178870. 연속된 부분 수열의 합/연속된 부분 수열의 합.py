"""
변수명을 조금 더 신경 써서 해보자 

처음에는 분기를 세가지로 잡았는데 다음 두가지 문제가 발생
1. k와 같아졌을 때도 초기화하고 s += 1 해줘야 되는데 못함
2. e가 마지막일 때 한칸 더 가서 전체 정답에 sequence[e]를 더해줄 때 인덱스 오류 남
"""

"""
def solution(sequence, k):
    answer = []

    len_s = len(sequence)
    
    s = 0
    e = 0
    ps = sequence[0]
    pss = float('inf')
    while e < len_s:
        if ps == k:
            if pss > (e-s):
                answer = [s,e]
                pss = e-s
            ps -= sequence[s]
            s += 1
        elif ps < k:
            e += 1
            if e >= len_s:
                break
            ps += sequence[e]
        elif ps > k:
            ps -= sequence[s]
            s += 1
        
    return answer
"""
def solution(sequence, k):
    answer = []

    len_s = len(sequence)
    
    s = 0
    e = 0
    current_sum = sequence[0]
    best_len = float('inf')
    
    while e < len_s:
        if current_sum >= k:
            if current_sum == k:
                length = e - s
                if length < best_len:
                    answer = [s,e]
                    best_len = length
            current_sum -= sequence[s]
            s += 1
        else:
            e += 1
            if e >= len_s:
                break
            current_sum += sequence[e]
        
    return answer

