"""
from collections import defaultdict
def solution(k, tangerine):
    d = defaultdict(int)
    
    for t in tangerine:
        d[t] += 1
        
    counts = sorted(d.values(), reverse = True)
    
    total = 0
    answer = 0
    
    for count in counts:
        total += count
        answer += 1
        
        if total >= k:
            return answer
"""
from collections import Counter

def solution(k, tangerine):
    counts = sorted(Counter(tangerine).values(), reverse=True)

    total = 0

    for i, count in enumerate(counts, 1):
        total += count

        if total >= k:
            return i