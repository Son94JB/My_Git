import sys
input = sys.stdin.readline


def is_good(num_list, num):

    start = 0
    end = len(num_list) - 1

    while start < end:
        a = num_list[start] + num_list[end]
        if a > num:
            end -= 1
        elif a < num:
            start += 1
        elif a == num:
            return 1
    return 0


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0

if len(nums) <= 2:
    print(0)
else:
    for i in range(N):
        new = nums[:i] + nums[i+1:]
        count += is_good(new, nums[i])
    print(count)

