#  n을 최소 개수의 제곱수 합으로 표현했을 때, 그 최소 개수를 구하라
import math
n = int(input())  # 1 <= n <= 50000
#  결국 n**0.5 가 바로 정수가 되는 경우와 그렇지 않은 경우가 있다.


def solution(x):
    #  n이 제곱수인 경우(n = a**2)
    if int(math.sqrt(x)) == math.sqrt(x):
        return 1
    #  그렇지 않은 경우

    #  두 개의 제곱수의 합으로 표현가능한 경우
    #  = n - i**2 가 제곱수인 경우
    for i in range(1, int(math.sqrt(x)) + 1):
        if int(math.sqrt(x - i**2)) == math.sqrt(x - i**2):
            return 2
    #  세 개의 제곱수의 합으로 표현가능한 경우
    #  = n - i**2 - j**2 가 제곱수인 경우
    for i in range(1, int(math.sqrt(n)) + 1):
        for j in range(1, int(math.sqrt(n - i**2)) + 1):
            if int(math.sqrt(n - i**2 - j**2)) == math.sqrt(n - i**2 - j**2):
                return 3
    # 그 외의 경우는 4
    return 4


print(solution(n))
