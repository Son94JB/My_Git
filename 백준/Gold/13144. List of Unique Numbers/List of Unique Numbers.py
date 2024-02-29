N = int(input())
nums = list(map(int, input().split()))

count = 0
end = 0
check = [0] * (N + 1)

for start in range(N):
    while end < N and check[nums[end]] == 0:  # 중복되는 숫자가 등장하지 않는 한 end 포인터를 이동
        check[nums[end]] = 1
        end += 1

    count += end - start  # start부터 end까지의 구간에서 중복되지 않는 숫자의 개수를 더함

    check[nums[start]] = 0  # start 포인터를 이동하기 전에 해당 숫자의 등장 여부를 초기화

print(count)