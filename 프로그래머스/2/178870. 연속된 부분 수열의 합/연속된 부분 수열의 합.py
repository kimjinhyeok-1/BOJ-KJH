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