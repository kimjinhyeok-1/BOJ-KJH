"""
투포인터로 보석을 하나씩 넣기
1. 만약 보석이 4종류가 안된다면 하나 더 넣기
2. 만약 보석이 4종류 이상이면 앞에서부터 하나씩 빼기
3. 만약 보석이 4종류라면 e-s 값을 초기화 
"""
from collections import defaultdict

def solution(gems):
    answer = []
    set_gems = set(gems)
    total_len = len(set_gems)
    
    # 보석 개수 넣는 defaultdict
    gems_count = defaultdict(int)
    gems_count[gems[0]] += 1
    # 시작, 끝, 최소 구간 길이 정하기
    s = 0
    e = 0
    best_len = float('inf')
    
    while e < len(gems):
        len_gc = len(gems_count)
        if len_gc < total_len:
            e += 1
            if e >= len(gems):
                continue
            gems_count[gems[e]] += 1
            
        if len_gc >= total_len:
            if len_gc == total_len:
                current_len = e-s
                if best_len > current_len:
                    best_len = current_len
                    answer = [s+1,e+1]
            gems_count[gems[s]] -= 1
            if gems_count[gems[s]] == 0:
                del gems_count[gems[s]]
            s += 1
        
    return answer












