# 입력 받기
H, W = map(int, input().split())  # 2차원 세계의 세로 길이 H와 가로 길이 W 입력 받기
blocks = list(map(int, input().split()))  # 블록의 높이 정보 입력 받기

# 빗물이 고일 수 있는 총량을 저장할 변수
total_water = 0

# 각 위치에서 빗물 계산
for i in range(1, W - 1):  # 가장자리 블록은 빗물이 고일 수 없으므로 1부터 W-1까지 반복
    # 현재 위치에서 왼쪽 블록 중 가장 높은 블록 찾기
    left_max = max(blocks[:i])
    # 현재 위치에서 오른쪽 블록 중 가장 높은 블록 찾기
    right_max = max(blocks[i + 1:])

    # 현재 위치에서 고일 수 있는 빗물의 양 계산 (더 낮은 블록의 높이 - 현재 블록의 높이)
    water = min(left_max, right_max) - blocks[i]

    # 빗물의 양이 양수일 경우에만 더하기
    if water > 0:
        total_water += water

# 빗물의 총량 출력
print(total_water)
