# 요세푸스 -> n명이 원을 이루고 k번 째 사람을 제거
# 제거한 사람의 번호로 n명이 모두 제거될 때까지 실행했을 때, 제거되는 번호를 순서대로 나열한 것.

def josephus(n, k):
    answer = []

    pivot = k-1
    people = [i for i in range(1, n+1)]

    while people:
        answer.append(people[pivot])
        people.remove(people[pivot])
        if len(people) == 0:
            break
        pivot = (pivot + (k-1)) % len(people)

    formatted_result = f"<{', '.join(map(str, answer))}>"
    return formatted_result


n, k = map(int, input().split())
print(josephus(n, k))
