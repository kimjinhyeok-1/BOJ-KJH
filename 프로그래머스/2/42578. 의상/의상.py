from collections import defaultdict

def solution(clothes):
    dic = defaultdict(int)
    answer = 1
    
    for clothe, t in clothes:
        dic[t] += 1
    for d in dic.values():
        answer *= (d+1)
    return answer -1