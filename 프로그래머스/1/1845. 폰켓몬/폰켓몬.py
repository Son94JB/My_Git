def solution(nums):
    # N/2 개를 선택했을 때, 가장 다양한 숫자들을 포함할 때의 개수
    answer = 0
    temp = len(set(nums))
    if len(nums)//2 <= temp:
        answer = len(nums)//2
    else:
        answer = temp
    return answer