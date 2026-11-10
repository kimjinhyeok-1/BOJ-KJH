def solution(progresses, speeds):
    answer = []
    l = len(progresses)
    deploy_day = []
    
    for i in range(l):
        k = ((100 - progresses[i]) - 1)// speeds[i] + 1
        deploy_day.append(k)
    
    max_day = deploy_day[0]
    cnt = 1
    
    for i in range(1,l):
        next_day = deploy_day[i]
        if next_day <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            max_day = next_day
            cnt = 1
        if i == l-1:
            answer.append(cnt)
    
    return answer



