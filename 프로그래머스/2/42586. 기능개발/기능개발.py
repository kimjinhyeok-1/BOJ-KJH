def solution(progresses, speeds):
    l = len(progresses)
    deplo_day = []
    for i in range(l):
        k = (100-progresses[i] + speeds[i] -1) // speeds[i]
        deplo_day.append(k)   
    
    print(deplo_day)
    answer = []
    
    max_day = deplo_day[0]
    cnt = 1
    
    for i in range(1,l):
        if deplo_day[i] <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            max_day = deplo_day[i]
            cnt = 1
        if i == l-1:
            answer.append(cnt)
    return answer

# (a + b -1) //b
# 7, 3, 9