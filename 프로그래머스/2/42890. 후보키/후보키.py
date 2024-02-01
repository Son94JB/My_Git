import itertools


def solution(relations):
    row_num = len(relations)
    col_num = len(relations[0])

    # 후보키 리스트
    candidate_keys = []

    # 모든 속성의 조합을 구함
    for num in range(1, col_num + 1):
        for comb in itertools.combinations(range(col_num), num):
            # 유일성 검사
            temp = [tuple([item[i] for i in comb]) for item in relations]
            if len(set(temp)) == row_num:
                # 최소성 검사
                for key in candidate_keys:
                    if set(key).issubset(set(comb)):
                        break
                else:
                    candidate_keys.append(comb)

    return len(candidate_keys)