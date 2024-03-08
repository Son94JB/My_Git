N, M, L, K = map(int, input().split())

meteor = []
for _ in range(K):
    x, y = map(int, input().split())
    meteor.append((x, y))

# 별똥별의 x좌표를 기준으로 정렬
meteor.sort()

result = float('inf')  # 결과 값을 무한대로 초기화
for i in range(K):
    # 슬라이딩 윈도우의 왼쪽 범위를 설정
    left_range = meteor[i][0]
    # 슬라이딩 윈도우의 오른쪽 범위를 설정
    right_range = left_range + L

    # 슬라이딩 윈도우 내의 별똥별들을 저장할 리스트
    stars_in_window = []

    for j in range(i, K):
        if meteor[j][0] <= right_range:
            stars_in_window.append(meteor[j][1])

    # 슬라이딩 윈도우 내의 별똥별들을 y좌표를 기준으로 정렬
    stars_in_window.sort()

    # y축에 대해 슬라이딩 윈도우를 적용
    for j in range(len(stars_in_window)):
        upper_range = stars_in_window[j]
        lower_range = upper_range + L
        count = 0

        for star in stars_in_window[j:]:
            if star <= lower_range:
                count += 1
            else:
                break

        result = min(result, K - count)  # 트램펄린 안에 들어가지 못하는 별똥별의 최소 개수를 구함

print(result)
