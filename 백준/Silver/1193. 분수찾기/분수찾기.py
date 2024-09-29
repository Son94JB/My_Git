def find_fraction(number):
    n = 1
    while number > n:
        number -= n
        n += 1

    if n % 2:
        numerator = n - number + 1
        denominator = number

    else:
        numerator = number
        denominator = n - number + 1
        
    return f"{numerator}/{denominator}"


N = int(input())

print(find_fraction(N))
