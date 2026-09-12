from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque((p,i) for i,p in enumerate(priorities))
    
    while True:
        cur_p,i = q.popleft()
        if any(p[0] > cur_p for p in q):
            q.append((cur_p,i))
        else:
            answer += 1
            if location == i:
                return answer
    
    return answer