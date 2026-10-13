def solution(order):
    answer = 0
    stack = []
    idx = 0
    
    for box in range(1, len(order) + 1):
        stack.append(box)
        
        while stack and stack[-1] == order[idx]:
            stack.pop()
            idx += 1
    
    return idx