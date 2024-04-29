from string import ascii_uppercase

word = input()
alp_dict = {}

for c in ascii_uppercase:
    alp_dict[c] = 0

for i in word:
    if i.upper() in alp_dict:
        alp_dict[i.upper()] += 1

max_value = max(alp_dict.values())
max_keys = [k for k, v in alp_dict.items() if v == max_value]

if len(max_keys) > 1:
    print("?")
else:
    print(max_keys[0])