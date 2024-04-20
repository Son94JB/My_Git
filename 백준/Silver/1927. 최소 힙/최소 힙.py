import sys
input = sys.stdin.readline
# 완전 이진 트리여야 한다.
# 최소 힙은 부모 노드가 자식 노드보다 작거나 같아야한다.
# 힙에 데이터 삽입, 노드를 꺼내고 삭제, 힙 구조로 바꾸는 세 가지가 필요
# 근데 어차피 입력값을 추가하는 식이니까 삽입, 최소값 도출하는 함수 두 개만 있으면 될 듯

# 삽입 : 기존 힙 구조에 새로운 원소를 추가한다
def heappush(heap, n):
    heap.append(n)  # 새로운 노드 추가
    cur_idx = len(heap) - 1  # 새 노드의 인덱스
    while cur_idx > 0:
        parent = (cur_idx - 1) // 2  # 부모 노드의 인덱스
        if heap[parent] > heap[cur_idx]:  # 부모 노드가 더 크다면
            heap[parent], heap[cur_idx] = heap[cur_idx], heap[parent]  # 서로 바꾼다
            cur_idx = parent  # 그리고 인덱스 갱신
        else:  # 순서가 맞다면 break
            break


# 원소 추출(최소 힙)
def heappop(heap):
    if not heap:  # 만약 비어있다면 0을 반환
        return 0
    elif len(heap) == 1:  # 하나만 있다면 그것을 반환
        return heap.pop()

    pop_data, heap[0] = heap[0], heap.pop()  # 반환할 데이터(최소값)이 루트 노드, 마지막 값(최대값)
    current, child = 0, 1  # 현재 노드(최대값, heap[0])와 자식 노드(왼쪽 노드)의 인덱스
    while child < len(heap):  # 왼쪽 노드의 인덱스가 heap 길이보다 작으면 반복
        sibling = child + 1  # sibling 은 오른쪽 노드 인덱스
        if sibling < len(heap) and heap[child] > heap[sibling]:
            # 오른쪽 노드가 존재하고 왼쪽 노드보다 작다면
            child = sibling  # 바꿔준다(둘 중 더 작은 노드와 바꿔주기 위함)
        if heap[current] > heap[child]:  # 현재 노드가 왼쪽 노드보다 크다면
            heap[current], heap[child] = heap[child], heap[current]  # 서로 바꿔준다.
            current = child  # 인덱스를 갱신해준다.
            child = current * 2 + 1  # 이제 자식 노드는 현재 노드 * 2 + 1
        else:
            break
    return pop_data


N = int(input())
myheap = []
for _ in range(N):
    data = int(input())
    if data:
        heappush(myheap, data)
    else:
        print(heappop(myheap))