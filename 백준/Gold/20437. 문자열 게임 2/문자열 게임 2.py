def find_substring_lengths(s, k):
    from collections import defaultdict

    char_indices = defaultdict(list)
    for i, char in enumerate(s):
        char_indices[char].append(i)

    min_length = 10001
    max_length = 0

    for indices in char_indices.values():
        if len(indices) < k:
            continue

        for i in range(len(indices) - k + 1):
            substring_length = indices[i + k - 1] - indices[i] + 1
            min_length = min(min_length, substring_length)
            max_length = max(max_length, substring_length)

    if min_length == 10001:
        return -1, -1

    return min_length, max_length


t = int(input())
for _ in range(t):
    s = input()
    k = int(input())
    min_length, max_length = find_substring_lengths(s, k)
    if min_length == -1:
        print(-1)
    else:
        print(min_length, max_length)
