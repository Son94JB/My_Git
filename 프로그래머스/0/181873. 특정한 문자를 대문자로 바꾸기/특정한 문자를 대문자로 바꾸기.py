def solution(my_string, alp):
    if alp not in my_string:
        return my_string

    my_string = my_string.replace(alp, alp.upper())

    return my_string
