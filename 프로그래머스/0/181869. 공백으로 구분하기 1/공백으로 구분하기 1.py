def solution(my_string):
    answer = []
    temp = ""
    for i in range(len(my_string) + 1):
        if i < len(my_string):
            if my_string[i] != " ":
                temp += my_string[i]
                continue
            answer.append(temp)
            temp = ""
        if temp:
            answer.append(temp)
    return answer