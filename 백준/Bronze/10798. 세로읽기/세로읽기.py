data = []
result = []

for _ in range(5):
    words = list(input())
    data.append(words)

p = 0
while p < 15:
    for temp in data:
        if p < len(temp):
            result.append(temp[p])

    p += 1

result = ''.join(result)

print(result)