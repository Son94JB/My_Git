data = list(map(int, input().split()))
temp = 0
for num in data:
    temp += num ** 2

print(temp % 10)
