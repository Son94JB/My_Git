N, M = map(int, input().split())

pocketmon_dict = dict()

for i in range(N):
    pocketmon_name = input()
    pocketmon_dict[i+1] = pocketmon_name

reverse_pairs = {v: k for k, v in pocketmon_dict.items()}

for i in range(M):
    quiz = input()
    if quiz.isdigit():
        print(pocketmon_dict[int(quiz)])
    else:
        print(reverse_pairs[quiz])
