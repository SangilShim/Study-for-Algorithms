
# 내풀이
def solution(progresses, speeds):
    Day = []
    for i in range(len(progresses)):
        x = float(((100-progresses[i])/speeds[i]))
        y = round(x+0.5)
        Day.append(y)
    answer = []
    count = 1
    first_day = Day[0]
    for i in range(1,len(Day)):
        if Day[i] <= first_day:
            count += 1
        elif Day[i] > first_day:
            answer.append(count)
            count = 1
            first_day = Day[i] 
    answer.append(count)

    return answer
  
  
