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
