def find_substring_lengths(s, k):

    min_length = 10001
    max_length = 0

    for char in set(s):
        indices = [i for i, x in enumerate(s) if x == char]
        if len(indices) < k:
            continue

        for i in range(len(indices) - k + 1):
            substring_length = indices[i + k - 1] - indices[i] + 1
            min_length = min(min_length, substring_length)
            max_length = max(max_length, substring_length)

    if min_length == 10001:
        return -1, -1

    return min_length, max_length


for _ in range(int(input())):

    word = input()
    k = int(input())
    answer1, answer2 = find_substring_lengths(word, k)
    if answer1 == -1:
        print(-1)
    else:
        print(answer1, answer2)
