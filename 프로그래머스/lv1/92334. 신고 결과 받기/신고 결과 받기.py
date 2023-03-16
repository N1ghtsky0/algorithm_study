def solution(id_list, report, k):
    answer = []
    _, result = init_dict(id_list)
    report_dict, reported = init_dict(id_list)
    report = set(report)
    
    for item in report:
        R, be_R = item.split()
        if be_R not in report_dict[R]:
            report_dict[R].append(be_R)
            reported[be_R] += 1

    for item in id_list:
        if reported[item] >= k:
            for item2 in id_list:
                if item in report_dict[item2]:
                    result[item2] += 1
    answer = list(result.values())
    return answer

def init_dict(id_list):
    report_dict = {}
    reported = {}
    for id in id_list:
        report_dict[id] = []
        reported[id] = 0
    return report_dict, reported