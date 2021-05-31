
# 첫번째 시도
# 앞서 가던 차가 다리를 건넜을 때의 상황을 생각하지 못하였다.
def solution(bridge_length, weight, truck_weights):
    j = 0
    time = 0
    for i in range(len(truck_weights)):
        if j == 0:
            j += truck_weights[i]
            if j < weight:
                time += bridge_length
            elif j == weight:
                time += bridge_length
                j = 0
        elif j > 0 and j < weight:
            j += truck_weights[i]
            if j > weight:
                j = truck_weights[i]
                time += bridge_length
            elif j < weight:
                time += 1
            elif j == weight:
                time += 1
                j = 0   

    time += 1
    answer = time
    return answer
  
# 구글링 풀이
# 스택을 쌓아서 1씩 더해주기 
time = 0
q = [0] * bridge_length

    
while q:
    time += 1
    q.pop(0)  # 데큐에서 popleft() 한거랑 똑같다. 하지만 데큐가 시간복잡도가 훨 좋다
    if truck_weights:
        if sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)
    
print(time)
