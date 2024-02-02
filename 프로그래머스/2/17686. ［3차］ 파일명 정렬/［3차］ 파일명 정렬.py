def solution(files):

    # 입력받은 파일 이름들을 분류한다.
    # 모두 소문자로 바꿔주고 -> x 원본명으로 정렬해야한다.
    # 숫자가 나올 때까지 자르고
    # 숫자가 나오면 해당 숫자는 NUMBER로 분류한다.
    # 어차피 TAIL은 분류랑 무관

    file_info = []
    for file in files:
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                tail = file[i:]
                break

        for i in range(len(tail)):
            if not tail[i].isdigit():
                number = tail[:i]
                tail = tail[i:]
                break
        else:
            number = tail
            tail = ''

        file_info.append((file, head.lower(), int(number)))

    file_info.sort(key=lambda x: (x[1], x[2]))
    answer = [file[0] for file in file_info]

    return answer
