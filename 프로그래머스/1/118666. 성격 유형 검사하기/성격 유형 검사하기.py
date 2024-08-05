def solution(survey, choices):
    answer = ''
    # 선택 1 2 3 4 5 6 7 -> 점수 3 2 1 0 1 2 3
    # RT, CF, JM, AN 이 각각의 쌍
    result = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = [3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        if choices[i] < 4:
            result[survey[i][0]] += score[choices[i] - 1]
        elif choices[i] > 4:
            result[survey[i][1]] += score[choices[i] - 1]
        else:
            continue

    if result['R'] == result['T']:
        answer += 'R'
    else:
        answer += 'R' if result['R'] > result['T'] else 'T'

    if result['C'] == result['F']:
        answer += 'C'
    else:
        answer += 'C' if result['C'] > result['F'] else 'F'

    if result['J'] == result['M']:
        answer += 'J'
    else:
        answer += 'J' if result['J'] > result['M'] else 'M'

    if result['A'] == result['N']:
        answer += 'A'
    else:
        answer += 'A' if result['A'] > result['N'] else 'N'

    return answer