def sol(idx, result):
    numbers.add(result)
    if idx > N-1:
        return

    sol(idx+1, result+num[idx])
    sol(idx+1, result)


N = int(input())
num = list(map(int, input().split()))
numbers = set()

sol(0, 0)
for i in range(max(numbers)+2):
    if i not in numbers:
        print(i)
        break
