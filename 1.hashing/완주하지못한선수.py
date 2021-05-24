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
