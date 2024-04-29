number = [0] * 10
num = 1
for _ in range(3):
    num *= int(input())

for n in str(num):
    number[int(n)] += 1

for i in range(10):
    print(number[i])