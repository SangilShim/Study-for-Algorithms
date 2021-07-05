# 내 풀이
def solution(array, commands):
    answer = []
    for i in commands:
        t = array[i[0]-1:i[1]]
        t.sort()
        r = t[i[2]-1]
        answer.append(r)
    
    return answer

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

# 개선된 풀이 : 한줄에 때려박아보자 sorted를 이용

answer = []
for i in commands:
    answer.append(sorted(array[i[0]-1:i[1]])[i[2]-1])
print(answer)


# 인상적인 풀이
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
