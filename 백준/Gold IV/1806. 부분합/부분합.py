def solution(n, s, sequence):

    p1 = 0
    p2 = 0
    sector_sum = 0
    
    min_length = float('inf')

    while True:
        if sector_sum >= s:
            min_length = min(min_length, p2-p1)
            sector_sum -= sequence[p1]
            p1 += 1
        elif p2 == n:
            break
        else:
            sector_sum += sequence[p2]
            p2 += 1

    if min_length == float('inf'):
        answer = 0
    else:
        answer = min_length

    return answer


N, S = map(int, input().split())
seq = list(map(int, input().split()))
print(solution(N, S, seq))
