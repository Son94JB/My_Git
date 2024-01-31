def solution(msg):
    alp_dict = {chr(64 + i): i for i in range(1, 27)}
    answer = []
    w = c = 0

    while True:
        c += 1

        if c == len(msg):
            answer.append(alp_dict[msg[w:c]])
            break

        if msg[w:c+1] not in alp_dict:
            alp_dict[msg[w:c+1]] = max(alp_dict.values()) + 1
            answer.append(alp_dict[msg[w:c]])
            w = c

    return answer
