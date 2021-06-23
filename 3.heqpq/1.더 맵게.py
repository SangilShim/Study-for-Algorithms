# 1차 시도 내풀이 (택도 없음)

scoville = [1, 1, 2, 2, 1, 9, 10, 12]
K = 7
count = 0
mix_list = []
for i in scoville:
    if i >= K:
        pass
    else:
        mix_list.append(i)
while True:
    mix_list.sort()
    for k in mix_list:
        if k >= K:
            break
        else:
            pass
    if len(mix_list) == 1:
        count = -1
        break
    else:
        o = mix_list[0] + (mix_list[1]*2)
        mix_list.append(o)
        mix_list = mix_list[2:]
        count += 1
            
print(count)

# 2차시도

import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        min1 = heapq.heappop(scoville)
        
        if min1 >= K:
            answer = count
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + (min2*2))
            count += 1
            
    if scoville[0] > K:
        return answer
            
    else:
        return -1
#채점 결과
정확성: 71.4
효율성: 23.8
합계: 95.2 / 100.0
