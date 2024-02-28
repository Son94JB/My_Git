result = [[0, 0] for _ in range(10001)]

result[1][0] = 0
result[1][1] = 0

result[2][0] = 1
result[2][1] = 0

result[3][0] = 1
result[3][1] = 1


def solution():
    for i in range(4, 10001):
        result[i][0] = i//2
        result[i][1] = result[i-3][0] + result[i-3][1] + 1


solution()
for _ in range(int(input())):
    N = int(input())
    print(result[N][0] + result[N][1] + 1)

