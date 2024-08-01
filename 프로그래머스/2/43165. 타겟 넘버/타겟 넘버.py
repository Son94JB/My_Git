def solution(numbers, target):
    def dfs(index, current_sum):
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 현재 합계가 타겟과 같다면 경우의 수를 하나 증가
            return 1 if current_sum == target else 0

        # 현재 숫자에 +를 붙이는 경우와 -를 붙이는 경우 모두 탐색
        count = 0
        count += dfs(index + 1, current_sum + numbers[index])
        count += dfs(index + 1, current_sum - numbers[index])

        return count

    return dfs(0, 0)

