def check(key, obj):
    count = 0
    for i in range(min(len(key), len(obj))):
        if key[i] == obj[i]:
            count += 1
        else:
            break
    return count


N = int(input())
words = [input() for _ in range(N)]

sorted_words = sorted(list(enumerate(words)), key=lambda x: x[1])

prefix = [0] * (N+1)
max_length = 0

for i in range(N-1):
    max_length = max(max_length, check(sorted_words[i][1], sorted_words[i+1][1]))
    prefix[sorted_words[i][0]] = max(prefix[sorted_words[i][0]], check(sorted_words[i][1], sorted_words[i+1][1]))
    prefix[sorted_words[i+1][0]] = max(prefix[sorted_words[i+1][0]], check(sorted_words[i][1], sorted_words[i+1][1]))

temp = 0
for i in range(N):
    if temp == 0:
        if prefix[i] == max_length:
            temp = words[i]
            print(temp)
            pre = words[i][:max_length]
    else:
        if prefix[i] == max_length and words[i][:max_length] == pre:
            print(words[i])
            break
