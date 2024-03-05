import math


def size(n):
    h = math.ceil(math.log(n)/math.log(2)) + 1
    return math.pow(2, h) - 1


def init(node, start, end):  # left, right == start, end
    if start == end:
        tree[node] = nums[start]
    else:
        mid = (start + end) // 2
        tree[node] = init(node*2, start, mid) + init(node*2 + 1, mid + 1, end)
    return tree[node]


# 기존 값과의 차이를 사용하는 유형
# 이 방법이 더 효율적이라고 함
def update(start, end, node, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, node*2, idx, diff)
        update(mid+1, end, node*2+1, idx, diff)


# 현재 노드의 포용범위 start, end
# 구하려는 구간 left, right
def cal(start, end, left, right, node):
    if left > end or start > right:
        return 0
    if start >= left and right >= end:
        return tree[node]
    mid = (start + end) // 2
    return cal(start, mid, left, right, node * 2) + cal(mid + 1, end, left, right, node * 2 + 1)


N, M, K = map(int, input().split())  # 수의 개수, 변경이 일어나는 횟수, 구간 합을 구하는 횟수
nums = [int(input()) for _ in range(N)]
tree = [0] + [0] * int(size(len(nums)))

init(1, 0, len(nums) - 1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - nums[b]
        nums[b] = c
        update(0, len(nums) - 1, 1, b, diff)
    else:
        print(cal(0, len(nums) - 1, b-1, c-1, 1))
