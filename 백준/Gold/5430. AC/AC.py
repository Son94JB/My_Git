# R 뒤집기
# D 첫 수 버리기
# 빈 배열에서 D를 수행하면 error
from collections import deque

t = int(input())

for _ in range(t):

    functions = input()
    num = int(input())
    data = input()[1:-1].split(',')
    data = deque(data)

    r_flag = 0

    if num == 0:
        data = []

    for function in functions:
        if function == "R":
            r_flag += 1

        elif function == "D":
            if data:
                if r_flag % 2 == 0:
                    data.popleft()
                else:
                    data.pop()
            else:
                print("error")
                break
    else:
        if r_flag % 2 == 0:
            print("[" + ",".join(data) + "]")
        else:
            data.reverse()
            print("[" + ",".join(data) + "]")
