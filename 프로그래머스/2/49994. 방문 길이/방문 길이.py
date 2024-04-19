def solution(dirs):
    answer = 0
    # UDLR 각각 상하좌우로 한 칸씩 가는 명령어
    # 입력이로 위의 4가지 문자로 이루어진 문자열을 받는다.
    # 명령어 순서대로 움직인 후, 중복되지 않는 길이를 구한다.
    # dirs의 길이는 500 이하의 자연수이다.
    visited = set()

    cur_x = 0
    cur_y = 0

    nxt_x = 0
    nxt_y = 0

    for dir in dirs:
        if dir == 'U':
            nxt_y = cur_y + 1
        elif dir == 'D':
            nxt_y = cur_y - 1
        elif dir == 'L':
            nxt_x = cur_x - 1
        elif dir == 'R':
            nxt_x = cur_x + 1

        if -5 <= nxt_x <= 5 and -5 <= nxt_y <= 5:  # 범위 내
            if (cur_x, cur_y, nxt_x, nxt_y) not in visited and (nxt_x, nxt_y, cur_x, cur_y) not in visited:
                # 해당 방향으로 방문 기록이 없다면
                visited.add((cur_x, cur_y, nxt_x, nxt_y))
            # 이동 후 다시 현재 포인트를 바꿔준다.
            cur_x = nxt_x
            cur_y = nxt_y

        else:  # 범위 밖이라면 이동하지 않는다.
            nxt_x = cur_x
            nxt_y = cur_y

        # 순환은 어떻게 해결하지?
        # 한 바퀴 돌아오는건 만약 URDL이라면
        # visited에는 4개의 점이고 거리는 4인데
        # URDR이라면 점은 5개이고 거리는 4이다.
        # 이전의 진행방향도 저장하면 되겠다.

    answer = len(visited)
    return answer