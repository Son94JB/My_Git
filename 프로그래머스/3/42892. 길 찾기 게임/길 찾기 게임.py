from sys import setrecursionlimit
setrecursionlimit(10000)
# 지훈아 음침하게 남의 코드 염탐이나 하고 말이야


def make_tree(info):
    result = sorted(sorted([(x, y, i+1) for i, (x, y) in enumerate(info)]))
    return result


def solution(nodeinfo):
    answer = [[], []]
    # 입력받은 데이터로 이진트리화 한다.
    # 전위순회(root, left, right)와 후위순회(left, right, root)를 해준다.
    # 전/후위순회할 때 따로 함수로 만들면 결과값을 따로 저장하기 번거로우니 한 함수에 몰아주자
    # y값이 가장 큰 노드를 기준으로 왼쪽 오른쪽 구분가능
    nodes = make_tree(nodeinfo)

    def recur(info):
        if info:
            highest = (0, -1, 0)  # 루트노드 찾기 (인덱스, y값, 노드번호)
            for idx, (x, y, n) in enumerate(info):
                if y > highest[1]:
                    highest = (idx, y, n)

            answer[0].append(highest[-1])
            left, right = info[:highest[0]], info[highest[0]+1:]
            recur(left)
            recur(right)
            answer[1].append(highest[-1])

    recur(nodes)

    return answer
