def prev_command(cur_pos, op_start, op_end):
    minutes = int(cur_pos[:2])
    seconds = int(cur_pos[3:])
    cur_time = minutes * 60 + seconds

    op_start_time = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_time = int(op_end[:2]) * 60 + int(op_end[3:])

    # 현재 위치가 오프닝 구간에 있을 경우
    if op_start_time <= cur_time <= op_end_time:
        cur_time = op_end_time

    cur_time -= 10

    # 다시 오프닝 구간 확인
    if op_start_time <= cur_time <= op_end_time:
        cur_time = op_end_time

    # 음수일 경우
    if cur_time < 0:
        return "00:00"

    return format_time(cur_time)

def next_command(cur_pos, video_len, op_start, op_end):
    minutes = int(cur_pos[:2])
    seconds = int(cur_pos[3:])
    cur_time = minutes * 60 + seconds

    op_start_time = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_time = int(op_end[:2]) * 60 + int(op_end[3:])
    max_time = int(video_len[:2]) * 60 + int(video_len[3:])

    # 현재 위치가 오프닝 구간에 있을 경우
    if op_start_time <= cur_time <= op_end_time:
        cur_time = op_end_time

    cur_time += 10

    # 동영상 끝을 초과할 경우
    if cur_time >= max_time:
        return video_len

    # 다시 오프닝 구간 확인
    if op_start_time <= cur_time <= op_end_time:
        return op_end

    return format_time(cur_time)

def format_time(cur_time):
    minutes = cur_time // 60
    seconds = cur_time % 60

    return f"{minutes:02}:{seconds:02}"

def solution(video_len, pos, op_start, op_end, commands):
    # 전체 동영상 길이, 현재 위치, 오프닝 시작, 오프닝 끝, 명령어
    # next와 prev로 이루어진 명령어들이 있다. 각각 10초 앞뒤로 가는 명령어이다.
    # 만약 10초 전에 동영상 시작 시간보다 작다면 제일 시작부분으로 간다.
    # 만약 10초 후가 동영상 끝보다 크다면 제일 끝부분으로 간다.
    # 만약 오프닝에서 next를 한다면 오프닝 끝부분으로 간다.

    result = pos
    for command in commands:
        if command == "prev":
            result = prev_command(result, op_start, op_end)
        else:
            result = next_command(result, video_len, op_start, op_end)

    answer = result

    return answer
