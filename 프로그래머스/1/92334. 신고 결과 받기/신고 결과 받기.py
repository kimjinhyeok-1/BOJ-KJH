def solution(id_list, report, k):
    n = len(id_list)
    person_list = {name:idx for idx, name in enumerate(id_list)}
    result = [0] * n
    answer = [0] * n
    
    report_set = set(report)
    
    for reports in report_set:
        report_p, reported_p = reports.split()
        result[person_list[reported_p]] += 1
    
    for reports in report_set:
        a,b = reports.split()
        if result[person_list[b]] >= k:
            answer[person_list[a]] += 1
        
    
    return answer