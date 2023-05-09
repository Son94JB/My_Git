a, b, c, d, e = map(int,input().split())
count = 0
for num in range(1, 10000000):
    count = 0
    if num % a == 0: count += 1
    if num % b == 0: count += 1
    if num % c == 0: count += 1
    if num % d == 0: count += 1
    if num % e == 0: count += 1
    if count > 2:
        print(num)
        break