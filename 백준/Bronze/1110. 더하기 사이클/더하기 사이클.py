number = input()
target = number
count = 0

if len(number) == 1:
    number = "0" + number

while True:
    temp = int(number[0]) + int(number[1])
    temp = str(temp)
    result = number[1] + temp[-1]

    count += 1
    if int(result) == int(target):
        break

    number = result

print(count)