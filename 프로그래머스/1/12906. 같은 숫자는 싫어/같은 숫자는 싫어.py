def solution(arr):

    stack = [arr[0]]
    for i in range(1, len(arr)):
        if stack[-1] != arr[i]:
            stack.append(arr[i])

    if stack[-1] != arr[-1]:
        stack.append(arr[-1])

    answer = stack

    return answer