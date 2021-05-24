[1차 시도]
def solution(phone_book):
    n = 0
    count = 0
    for i in phone_book:
        i = i[:-1]
        for j in phone_book[n+1:]:
            if i == j[:len(i)]:
                count += 1
        n += 1

    return not count >= 1
 
채점 결과
정확성: 66.7
효율성: 0.0
합계: 66.7 / 100.0

# 구글링 풀이

def solution(phone_book):
    phone_book.sort()
    for a,b in zip(phone_book,phone_book[1:]):
        if b.startswith(a):
            return False 

    return True


def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break
    return answer

# 해쉬를 이용한 풀이

