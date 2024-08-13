def solution(id_list, report, k):
    # report를 통해 신고자 - 피신고자 의 딕셔너리를 만든다.
    # 신고자 key가 피신고자 value를 가진다.
    # id_list로 사람들의 신고 당한 횟수를 카운트하는 딕셔너리를 만든다.
    # 각 key들의 value를 신고받은 횟수별로 카운트해준다.
    answer = [0] * len(id_list)

    report_state = {key: [] for key in id_list}
    report_result = {key: 0 for key in id_list}

    for data in report:
        reporter, reportee = data.split()
        if reportee not in report_state[reporter]:
            report_state[reporter].append(reportee)

    for temp in report_state.values():
        if not temp:
            continue
        for name in temp:
            report_result[name] += 1

    for reporter in id_list:
        for reportee in report_state[reporter]:
            if report_result[reportee] >= k:
                answer[id_list.index(reporter)] += 1

    return answer