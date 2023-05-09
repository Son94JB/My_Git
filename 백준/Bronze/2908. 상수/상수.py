num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])

if num1 > num2:
    ans = num1
else:
    ans = num2

print(ans)
