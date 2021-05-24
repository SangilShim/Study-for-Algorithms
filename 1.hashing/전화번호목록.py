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
