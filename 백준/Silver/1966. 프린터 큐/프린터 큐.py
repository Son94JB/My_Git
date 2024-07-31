from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # 문서의 개수 n, 프린트 순서가 궁금한 문서 m
    importance = list(map(int, input().split()))  # 중요도 리스트

    # (중요도, 인덱스) 형태로 큐에 저장
    queue = deque((importance[i], i) for i in range(n))
    print_order = 0

    while queue:
        current = queue.popleft()  # 현재 문서 꺼내기
        # 현재 문서보다 중요도가 높은 문서가 있는지 확인
        if any(current[0] < doc[0] for doc in queue):
            queue.append(current)  # 중요도가 낮으면 큐의 뒤로 보낸다
        else:
            print_order += 1  # 문서가 출력되면 출력 순서 증가
            if current[1] == m:  # 출력된 문서가 우리가 찾는 문서인지 확인
                print(print_order)
                break
