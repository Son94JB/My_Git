def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_remains = sum(deliveries)
    pickup_remains = sum(pickups)

    # 트럭이 가장 멀리 가야 할 집을 찾기 위한 인덱스
    delivery_index = n - 1
    pickup_index = n - 1

    while delivery_remains > 0 or pickup_remains > 0:
        # 현재 트럭의 최대 이동 거리
        move_dist = 0

        # 배달해야 할 상자가 있는 가장 먼 집을 찾음
        while delivery_index >= 0 and deliveries[delivery_index] == 0:
            delivery_index -= 1
        if delivery_index >= 0:
            move_dist = max(move_dist, delivery_index + 1)

        # 수거해야 할 상자가 있는 가장 먼 집을 찾음
        while pickup_index >= 0 and pickups[pickup_index] == 0:
            pickup_index -= 1
        if pickup_index >= 0:
            move_dist = max(move_dist, pickup_index + 1)

        # 이동 거리 추가 (왕복 거리이므로 2배)
        answer += move_dist * 2

        # 현재 트럭에 남은 용량
        current_cap = cap

        # 배달 처리
        while current_cap > 0 and delivery_index >= 0:
            if deliveries[delivery_index] > 0:
                if deliveries[delivery_index] <= current_cap:
                    current_cap -= deliveries[delivery_index]
                    delivery_remains -= deliveries[delivery_index]
                    deliveries[delivery_index] = 0
                else:
                    deliveries[delivery_index] -= current_cap
                    delivery_remains -= current_cap
                    current_cap = 0
            if deliveries[delivery_index] == 0:
                delivery_index -= 1

        # 수거 처리
        current_cap = cap
        while current_cap > 0 and pickup_index >= 0:
            if pickups[pickup_index] > 0:
                if pickups[pickup_index] <= current_cap:
                    current_cap -= pickups[pickup_index]
                    pickup_remains -= pickups[pickup_index]
                    pickups[pickup_index] = 0
                else:
                    pickups[pickup_index] -= current_cap
                    pickup_remains -= current_cap
                    current_cap = 0
            if pickups[pickup_index] == 0:
                pickup_index -= 1

    return answer