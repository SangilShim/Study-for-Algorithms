# 네번째 풀이만에 정답, 4시간 반 소요
# 튜플, zip에 대해 더 자세히 알 수 있었다.

# 첫번째 시도
j = []
for i in range(len(priorities)):
    j.append(i)
m = max(priorities)
r = priorities.index(m)
if r == 0:
    unreal = j[r:]
elif r == len(j):
    unreal = j[r] + j[:r]
else:
    unreal = j[r:] + j[:r]
h = j[location]
answer = unreal.index(h) + 1
print(answer)

# 최대값이 여러개일 경우를 생각못했다.

# 두번째 시도
j = []
strong = []
weak = []
m = max(priorities)
for i in range(len(priorities)):
    j.append(i)
for i in j:
    if priorities[i] == m:
        q = j[i]
        strong.append(q)
    else:
        k = j[i]
        weak.append(k)
real_list = strong + weak
e = j[location]
answer = real_list.index(e)
print(answer)

# 이것은 가장 큰 값은 잘 걸러냈지만 그 뒤로는 고려를 안해줬다. 이때 내가 문제를 잘 못 이해했다는 것을 깨달았다.

# 세번째 시도
# 4시간경과.. 최대값이 여러개인 값을 값일 경우와, 한개일 때를 나눠서 기괴하게 해봤지만, 정확도 55점 ㅋㅋㅋ미쳐버릴거같다
def solution(priorities, location):
    j = []
    v= []
    m = max(priorities)
    count = 0
    for i in range(len(priorities)):
        j.append(i)
    for i in priorities:
        if i == m:
            count += 1
        else:
            pass
    if count == 1:
        r = priorities.index(m)
        if r == 0:
            unreal = j[r:]
        elif r == len(j):
            unreal = j[r] + j[:r]
        else:
            unreal = j[r:] + j[:r]
        h = j[location]
        answer = unreal.index(h) + 1
        return answer
    else:
        for pair in zip(priorities, j):
            v.append(pair)
        v.sort(key=lambda x:(-x[0],x[1]))
        b = [x[1] for x in v]
        answer = b.index(location) + 1
        return answer
      
  # 네번째 시도 -> 정답!!!!!!!
  
  def solution(priorities, location):
    j = []
    v= []
    final_data = []
    for i in range(len(priorities)):
        j.append(i)
    for pair in zip(priorities, j):
        v.append(pair)
    for i in range(len(v)):
        b = [x[0] for x in v]
        c = max(b)
        r = b.index(c)
        t = v[r]
        final_data.append(t)
        v = v[r+1:] + v[:r]

    s = [x[1] for x in final_data]
    answer = s.index(location) + 1
    return answer
