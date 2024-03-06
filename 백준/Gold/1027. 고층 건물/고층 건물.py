N = int(input())
buildings = list(map(int, input().split()))

# 두 지붕을 잇는 선분이 다른 건물과 지나치거나 접하지 않아야 한다.
# 기준 건물에서 봐야한다.
# 기울기를 고려해야할듯
# 기울기를 구하는 함수랑, 점 두 개가 주어질 때, 해당 점 사이에 걸리는 것 없이
# 선분이 이어지는지 확인하는 함수 두 개가 필요할 듯


def tangent(x1, y1, x2, y2):  # 두 점 a와 b 사이의 기울기
    result = (y2 - y1) / (x2 - x1)
    return result


max_count = 0
# 기준이 되는 건물에서 좌우로 각각 검사해야 함
for i in range(N):
    count = 0
    left_slope = float('inf')
    right_slope = -float('inf')

    for j in range(i-1, -1, -1):
        temp_slope = tangent(i+1, buildings[i], j+1, buildings[j])
        if temp_slope < left_slope:
            left_slope = temp_slope
            count += 1

    for j in range(i+1, N):
        temp_slope = tangent(i+1, buildings[i], j+1, buildings[j])
        if temp_slope > right_slope:
            right_slope = temp_slope
            count += 1

    max_count = max(count, max_count)


print(max_count)
