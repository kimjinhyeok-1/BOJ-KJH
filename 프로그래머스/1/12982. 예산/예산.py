def solution(d, budget):
    answer = 0
    
    sorted_d = sorted(d)
    
    for i in range(len(d)):
        left = budget - sorted_d[i]
        
        if left < 0:
            break
        
        answer += 1
        budget -= sorted_d[i]
    return answer