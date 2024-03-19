# 다이아, 철, 돌
# 동/하위 광물은 피로도가 1 소모
# 상위는 *5 씩

# 각 곡괭이는 최대 5회 사용가능
# 한 번 사용하면 무조건 5회 사용해야한다.
# 최소 피로도 구하기

def solution(picks, minerals):
    answer = 0
    # 곡괭이의 총 수가 촤대 15
    # 모든 경우의 수를 구해서 실행?

    # 광물들을 5개씩 나눠서 다이아가 많은 구간을 좋은 곡괭이 순으로?
    # 광물을 5개 단위로 나누고 곡괭이의 개수만큼만 선택
    diamond_pickax, iron_pickax, stone_pickax = picks

    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)][:sum(picks)]

    # 광물을 다이아몬드, 철, 돌의 개수에 따라 내림차순으로 정렬
    minerals.sort(key=lambda x: (x.count("diamond"), x.count("iron"), x.count("stone")), reverse=True)
    fatigue = 0

    for mineral in minerals:
        if diamond_pickax > 0:
            for mnl in mineral:
                fatigue += cal_fatigue('diamond', mnl)
            diamond_pickax -= 1

    # 철 곡괭이가 있으면 사용
        elif iron_pickax > 0:
            for mnl in mineral:
                fatigue += cal_fatigue('iron', mnl)
            iron_pickax -= 1

        elif stone_pickax > 0:
            for mnl in mineral:
                fatigue += cal_fatigue('stone', mnl)
            stone_pickax -= 1

    answer = fatigue
    return answer


def cal_fatigue(pick, mineral):  # 피로도 계산
    fatigue_map = {
        'diamond': {'diamond': 1, 'iron': 1, 'stone': 1},
        'iron': {'diamond': 5, 'iron': 1, 'stone': 1},
        'stone': {'diamond': 25, 'iron': 5, 'stone': 1}

    }
    return fatigue_map[pick][mineral]
