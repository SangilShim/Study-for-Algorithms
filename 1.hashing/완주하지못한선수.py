# 내풀이
# 테스트 3에서 결괏값이 왜 stanko가 나오는 걸까..

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a,b in zip(participant,completion):
        if a != b:
            return a
        else:
            return participant[-1]
            
 테스트 3
입력값 〉	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
기댓값 〉	"mislav"
실행 결과 〉	실행한 결괏값 "stanko"이(가) 기댓값 "mislav"와(과) 다릅니다.

# for 반복문이 제역학을 못해준다

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for a,b in zip(participant,completion):
        if a != b:
            return a
        
    return participant[-1]

# 스터디 박상민님 풀이
from collections import Counter

def solution(participant, completion):
    return list((Counter(participant) - Counter(completion)).keys())[0]

// Counter 끼리 연산이 되는것 같더라구요! 직접해보시면 뭔지 아실거에요! 

# 스터디 문준호님 풀이
def solution(participant, completion):
    hash ={}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    for i in completion:
        if hash[i] == 1: 
            del hash[i]
        else:
            hash[i] -= 1 
    answer = list(hash.keys())[0] 
    return answer

# 스터디 오다혜님 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    big = participant if len(participant) > len(completion) else completion
    small = participant if len(participant) < len(completion) else completion
    for i in range(len(small)):
        if(participant[i] != completion[i]):
            return big[i]
    return big[-1]
