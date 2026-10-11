# queue1 + queue2 + queue1 세 개 이어 붙이고 나서 처리
def solution(queue1, queue2):
    n = len(queue1)
    total_sum = sum(queue1) + sum(queue2)
    
    # 만약 총 합이 홀 수라면 정답 존재 X
    if total_sum % 2 != 0:
        return -1
    
    queue = queue1 + queue2 + queue1
    target = total_sum // 2
    
    s = 0
    e = n-1
    count = 0
    current_sum = sum(queue1)
                       
    while count < 4 * n:
        if current_sum == target:
            return count
        
        if current_sum > target:
            current_sum -= queue[s]
            s += 1
            
        else:
            e += 1
            current_sum += queue[e]
            
        count += 1
            
    return -1

