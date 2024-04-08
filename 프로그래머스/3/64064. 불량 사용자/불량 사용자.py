import itertools


def is_matching(u_id, b_id):  # 두 단어를 비교
    if len(u_id) != len(b_id):  # 애초에 길이가 다르면 False
        return False

    for u, b in zip(u_id, b_id):
        if b == '*':  # * 이라면 일단 넘어가고
            continue
        if u != b:  # 다른 글자가 있다면 False
            return False

    # 그 외의 경우는 *을 빼면 다 일치한다는 뜻
    return True


def solution(user_id, banned_id):
    # 불량 사용자의 아이디가 *로 가려져서 제공된다.
    # 해당 불량 사용자 리스트로 가능한 경우의 수를 구하는 것
    # 각 배열의 크기는 1 ~ 8이고 원소의 길이도 1 ~ 8이다. (단, len(user_id) >= len(banned_id))
    # 크기가 작으니 하나하나 검사해도 될 듯? 최악의 경우 64*64 정도?
    # 일단 banned_id 기준으로 user_id를 검사하면 될 듯
    possible_cmb = itertools.permutations(user_id, len(banned_id))  # user_id들로 불량 사용자 개수만큼으로 가능한 조합들
    valid_cmb = set()

    for cmb in possible_cmb:
        if all(is_matching(user, ban) for user, ban in zip(cmb, banned_id)):
            # 유효한 조합을 찾은 경우, 사용자 아이디 조합을 정렬하여 중복을 제거한 후 튜플로 변환
            # 이렇게 하면 동일한 조합이 여러 번 나오더라도 중복을 제거할 수 있다.
            valid_cmb.add(tuple(sorted(cmb)))

    answer = len(valid_cmb)
    return answer

