def solution(edges):
    answer = [0, 0, 0, 0]
    # 도넛 그래프 : n개의 정점, n개 간선 -> 다 하나씩 주고받기
    # 막대 그래프 : n개의 정점, n-1개 간선 -> 나가는 간선이 없는 노드가 하나씩 존재
    # 8자 그래프 : 2n+1개의 정점, 2n+2개 간선 -> 나가는 간선이 2개인 노드가 하나씩 존재

    # 각 노드에서 나가는 간선의 개수를 리스트(딕셔너리가 더 빠를 듯?)로 나타내고
    # 막대, 8자형 그래프 개수 구한 뒤 도넛 그래프 개수 구하기.
    nums = [num for temp in edges for num in temp]
    size = max(nums)

    ins = [0 for _ in range(size)]
    outs = [0 for _ in range(size)]

    for edge in edges:
        ins[edge[1] - 1] += 1
        outs[edge[0] - 1] += 1

    for i in range(len(outs)):
        if outs[i] == 1:
            continue
        elif outs[i] == 0:
            answer[2] += 1
        elif outs[i] == 2:
            if ins[i] > 0:
                answer[3] += 1
            else:
                answer[0] = i + 1
        elif outs[i] > 2:
            answer[0] = i + 1

    answer[1] = outs[answer[0] - 1] - (answer[2] + answer[3])

    return answer