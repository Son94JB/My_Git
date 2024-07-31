import itertools


def solution(users, emoticons):
    # 1. 이모티콘 플러스 가입자를 최대로
    # 2. 이모티콘 판매액을 최대로
    discount_percent = [10, 20, 30, 40]

    # n명에게 m개의 이모티콘을 할인 판매
    # 이모티콘마다 할인율은 다를 수 있음 (10, 20, 30, 40)
    # 사용자는 자신의 기준 할인율(1 <= 할인율 <= 40) 이상의 할인율을 가진 이모티콘을 구매한다.
    # 만약 총 금액이 기준 금액보다 높다면 이모티콘 플러스를 구매한다.
    # -> 할인시의 최소 금액과 최대 금액을 바탕으로 이모티콘 플러스 가입자 수를 구한다?

    # 할인율 4개 중 이모티콘 개수만큼 중복을 허용해 고르기
    k = len(emoticons)
    discount_lists = list(itertools.product(discount_percent, repeat=k))
    # 구한 리스트를 통해서 가격을 구하고 가격 별로 플러스 가입자와 총 판매액 구하기

    max_plus_subscribe = 0
    max_total_price = 0

    for discounts in discount_lists:
        total_price = 0
        plus_subscribe = 0

        for user in users:
            user_discount_allow, user_budget = user
            user_total_spent = 0

            for i in range(k):
                # 이모티콘 가격에 따른 할인 적용
                discount = discounts[i]
                discounted_price = emoticons[i] * (100 - discount) / 100

                # 사용자가 이모티콘을 구매할 수 있는지 확인
                if discount >= user_discount_allow:
                    user_total_spent += discounted_price

            # 사용자가 이모티콘 플러스를 구독할 수 있는지 확인
            if user_total_spent >= user_budget:
                plus_subscribe += 1
            else:
                total_price += user_total_spent

        # 최대 플러스 가입자 수와 최대 총 판매액 업데이트
        if plus_subscribe > max_plus_subscribe:
            max_plus_subscribe = plus_subscribe
            max_total_price = total_price
        elif plus_subscribe == max_plus_subscribe:
            max_total_price = max(max_total_price, total_price)

    answer = [max_plus_subscribe, max_total_price]  # [플러스 가입자 수, 이모티콘 총 판매액]
    return answer