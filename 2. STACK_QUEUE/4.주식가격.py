# 첫번째 시도
prices = [1, 2, 3, 2, 3]
answer = []
count = 0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        print(j)
        if prices[i] <= prices[j]:
            count += 1            
        else:
            pass
    answer.append(count)
    count = 0

print(answer)

정확성: 6.7
효율성: 0.0
합계: 6.7 / 100.0
  
# 두번째 시도 + 구글링

answer = [0] * len(prices)
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[i] <= prices[j]:
            answer[i] += 1            
        else:
            answer[i] += 1
            break
 채점 결과
정확성: 66.7
효율성: 33.3
합계: 100.0 / 100.0
