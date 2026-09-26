"""
접근 1: 완탐
- 완탐을 하게 되면 N이 20 K가 10만 되더라도 말이 안됨

접근 2: 그리디
- 앞에서부터 하나씩 보면서 현재 가장 뒷 숫자보다 내가 더 크면 나로 변경
- 근데 조건이 붙음 현재 아무것도 안 넣은 상태면 무조건 append
- k를 하나씩 줄이다가 k가 0보다 크지 않다면 종료
- 근데 이미 큰수로 모두 정렬이 되어있으면 마지막에 k개수만큼 마지막에서 제외해주기
"""
def solution(number, k):
    stack = []
    
    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    answer = "".join(stack)
        
    if k > 0:
        return answer[:-k]
    else:
        return answer