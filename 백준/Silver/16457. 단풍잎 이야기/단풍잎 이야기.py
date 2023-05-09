n, m, k = map(int, input().split())
skills = [tuple(map(int, input().split())) for i in range(m)]
batch = [0 for i in range(n)]
answer = 0

def pick(prev, idx):                # 2n 중 n 개를 재귀를 통해 중복 없이 뽑아 확인하는 함수(조합)
    if idx == n:                    # n 개를 다 뽑았다면 몇개의 퀘스트 수행 가능한지 확인
        tmp = set(batch)
        cnt = 0
        for sk in skills:           # 모든 요구 스킬을 확인하며
            for s in sk:            # 하나라도 사용하지 못하는 스킬이 포함되면 넘어감
                if s not in tmp:
                    break
            else:                   # 퀘스트 수행 가능시 +1
                cnt += 1
        global answer               # 최댓값 갱신
        if cnt > answer:
            answer = cnt
        return
    for i in range(prev+1, 2*n+1):  # 정렬된 순서대로 재귀 확인
        batch[idx] = i
        pick(i, idx+1)

pick(0, 0)
print(answer)