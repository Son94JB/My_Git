def solution(friends, gifts):
    # 선물을 주고받은 기록이 있다면, 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다.
    # 주고받은 기록이 없거나 같다면 선물 지수가 더 큰 사람이 더 작은 사람에게 선물을 하나 받는다.
    # 선물 지수 = (이번 달 준 선물의 수) - (이번 달 받은 선물의 수)
    # 만약 선물 지수도 모두 동일하다면 선물을 주고받지 않는다.
    # 위에서 설명한 규칙대로 다음 달에 선물을 주고받을 때, 선물을 가장 많이 받을 친구가 받을 선물의 수를 구하자.
    # friends는 모든 친구들 이름의 문자열
    # gifts는 A가 B에게 선물을 주는 형태의 문자열

    # friends와 gifts를 기준으로 2차원 배열을 만든다.
    # 가장 많이 선물을 준 사람을 찾는다.
    # 같거나 기록이 없다면 선물 지수를 구해준다.
    # 총으로 하는게 아니라 각각 친구를 대상으로
    size = len(friends)
    give_gift = list([0] * size for _ in range(size))  # i가 j에게 준 선물
    get_gift = list([0] * size for _ in range(size))  # i가 j에게 받은 선물
    result = [0] * size  # 결과, 받아야 하는 선물

    friends_dict = {}
    for i, name in enumerate(friends):
        friends_dict[name] = i

    for i in range(len(gifts)):
        a, b = gifts[i].split()
        give_gift[friends_dict[a]][friends_dict[b]] += 1
        get_gift[friends_dict[b]][friends_dict[a]] += 1

    for i in range(size):
        for j in range(size):
            if i == j:
                continue
            if give_gift[i][j]:  # j에게 준 선물이 있다면 비교해준다.
                if give_gift[j][i] < give_gift[i][j]:  # j가 i에게 준 선물보다 i가 j에게 준 선물이 더 많다면
                    result[i] += 1  # i가 받을 선물을 늘린다.
                elif give_gift[j][i] == give_gift[i][j]:  # 각자 준 선물이 같다면 각 지수를 비교해서
                    i_factor = sum(give_gift[i]) - sum(get_gift[i])
                    j_factor = sum(give_gift[j]) - sum(get_gift[j])
                    if i_factor > j_factor:  # 지수가 더 크다면 줄 선물을 추가한다.
                        result[i] += 1

            elif give_gift[i][j] == 0 and give_gift[j][i] == 0:  # 둘 다 선물을 주고 받지 않았다면
                i_factor = sum(give_gift[i]) - sum(get_gift[i])  # 지수를 비교해서
                j_factor = sum(give_gift[j]) - sum(get_gift[j])

                if i_factor > j_factor:  # 지수가 더 크다면 줄 선물을 추가한다.
                    result[i] += 1

    answer = 0

    for i in range(size):
        if result[i] > answer:
            answer = result[i]

    return answer

