def solution(a, b, g, s, w, t):
    # 새 왕국을 짓는데 필요한 금과 은을 전달할 수 있는 가장 빠른 시간을 구하는 것
    # 필요 금 a, 필요 은 b, 소유 금 g, 소유 은 s, 최대 운반가능 무게 w, 편도로 걸리는 시간 t
    # 각 i번째의 도시에 관한 정보, 금과 은 동시 운반 가능
    start = 0
    answer = end = (10 ** 9) * (10 ** 5) * 4  # 최악의 경우
    cities = len(g)

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(cities):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 왕복으로 걸리는 최대 제한 시간
            move_cnt = mid // (now_time * 2)

            # 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            # 주어지 시간 내 최대 적재 가능량 누적하기
            possible_move_weight = move_cnt * now_weight
            gold += now_gold if (now_gold < possible_move_weight) else possible_move_weight
            silver += now_silver if (now_silver < possible_move_weight) else possible_move_weight
            total += now_gold + now_silver if (now_gold + now_silver < possible_move_weight) else possible_move_weight

        # total이 a+b 보다 크거나 같으면서 금과 은의 누적 최대값이 a와 b보다 크거나 같아야 한다.
        # 만약 금과 은의 누적 최대값이 보내야만 하는 a,b보다 작다면 현재 시간 내 처리 불가능하다.
        if total >= a + b and gold >= a and silver >= b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    return answer