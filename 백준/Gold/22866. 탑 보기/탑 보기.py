import sys

input = sys.stdin.readline
N = int(input())
data = list(enumerate(map(int, input().split()), start=1))
count = [0] * (N + 1)
nearest = [float("inf")] * (N + 1)

# 건물 개수랑 가장 가까운 건물 번호 중 작은 번호 출력
# 자신의 높이보다 높은 건물만 보인다.
# 그리고 중간의 건물보다 낮은 건물도 안보인다.


def solution(buildings):
    visibles = []

    for idx, height in buildings:
        while visibles and visibles[-1][1] <= height:
            visibles.pop()

        count[idx] += len(visibles)
        if visibles and abs(visibles[-1][0] - idx) < abs(nearest[idx] - idx):
            nearest[idx] = visibles[-1][0]

        visibles.append((idx, height))


solution(data[:])
solution(data[::-1])

for i in range(1, N + 1):
    if count[i] == 0:
        print(count[i])
    else:
        print(count[i], nearest[i])

    # 만약 기준 건물 높이보다 높으면서
    # 기준 건물과 가까운 쪽에 자기보다 높은 건물이 없다면 보인다.
