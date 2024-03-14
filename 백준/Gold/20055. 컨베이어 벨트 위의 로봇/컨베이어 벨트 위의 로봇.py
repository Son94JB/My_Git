N, K = map(int, input().split())
durable = list(map(int, input().split()))

# 회전 -> 이동 -> 로봇추가 -> 내구도 검사 -> 반복
# 회전은 자동으로 한다.
# 이동은 가능할 때 한다. 이동 시, 내구도가 1 줄어든다.
# 다음 칸이 내구도가 1이상 && 로봇이 없는 경우 이동
# 내구도가 0인 칸이 K개 이상이면 정지한다.
# 모든 프로세스가 끝나면 한 단계가 지난 것.


def robot_moving(n, arr):  # 로봇이 움직이는 과정
    count = 0
    for i in range(n-1, -1, -1):
        if arr[i][1]:
            if arr[i+1][0] > 0 and not arr[i+1][1]:
                arr[i][1] -= 1  # 원래 칸의 로봇 제거
                arr[i+1][1] += 1  # 다음 칸으로 로봇 이동
                arr[i+1][0] -= 1  # 다음 칸의 내구도 -1
                if not arr[i+1][0]:  # 내구도가 0이라면 count를 올려준다.
                    count += 1

            if i == n-2 and arr[n-1][1]:  # 만약 내리는 칸에 로봇이 있다면
                arr[n-1][1] -= 1  # 내려준다.

    return count


def belt_moving(n, arr):  # 벨트가 움직이는 과정
    last = arr.pop()
    arr.insert(0, last)

    if arr[n-1][1]:  # 마지막 칸에 로봇이 있으면 내린다.
        arr[n-1][1] = 0


robots = [[x, 0] for x in durable]  # 로봇이 없는 처음 벨트 상황
stage = 0
zero_D = 0

while True:
    # 내구도가 깎이는 경우는 2가지
    # 로봇이 컨베이어 벨트에 올라올 때와 로봇이 이동할 때
    stage += 1
    belt_moving(N, robots)  # 벨트 이동
    zero_D += robot_moving(N, robots)  # 로봇 이동

    if robots[0][0]:  # 올리는 곳 내구도가 1이상이면
        robots[0][1] += 1  # 로봇 추가
        robots[0][0] -= 1  # 내구도 감소
        if robots[0][0] == 0:
            zero_D += 1

    if zero_D >= K:  # 내구도 0인 칸이 K개 이상이라면 종료
        break

print(stage)
