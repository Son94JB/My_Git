arr = []
for _ in range(10):
    n = int(input())
    arr.append(n % 42)

s_arr = set(arr)
print(len(s_arr))
