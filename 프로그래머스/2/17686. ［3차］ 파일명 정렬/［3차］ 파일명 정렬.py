def solution(files):
    def file_key(file):
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                tail = file[i:]
                break
        for i in range(len(tail)):
            if (not tail[i].isdigit()) or i == 5:
                number = tail[:i]
                tail = tail[i:]
                break
        else:
            number = tail
            tail = ''
        return (head.lower(), int(number))

    return [file for _, file in sorted(enumerate(files), key=lambda x: file_key(x[1]))]