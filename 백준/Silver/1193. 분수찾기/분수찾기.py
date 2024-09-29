N = int(input())
num = 1
if N == 1:
    print("1/1")
else:
    for i in range(2*N):
        if num + i <= N:
            num += i
            continue
        else:
            diff = N - num
            if i % 2:
                a = i - diff
                b = 1 + diff
            else:
                a = 1 + diff
                b = i - diff
        print(f"{a}/{b}")
        break

