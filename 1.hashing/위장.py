from collections import Counter

def solution(clothes):
    answer = 1
    kind = Counter([cloth[1] for cloth in clothes])
    
    for i in kind:
           answer *= (kind[i] + 1)
           
    answer -= 1
    
    return answer
