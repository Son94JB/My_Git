def solution(lottos, win_nums):
    # 로또의 최고 순위와 최저 순위를 반환
    # 0은 알아볼 수 없는 숫자
    rank = {  # 일치하는 숫자 개수: 등수
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    answer = []

    corrects = 0
    possibility = 0

    for num in lottos:
        if num in win_nums:
            corrects += 1
        elif num == 0:
            possibility += 1

    max_rank = rank[corrects + possibility]
    min_rank = rank[corrects]

    answer.append(max_rank)
    answer.append(min_rank)
    return answer