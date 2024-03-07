N = int(input())
nums = list(map(int, input().split()))
nums_sorted = sorted(nums)

count = 0
for i in range(N):
    left = 0
    right = N - 1
    while left < right:
        if right == i:
            right -= 1
        elif left == i:
            left += 1
        elif nums_sorted[left] + nums_sorted[right] < nums_sorted[i]:
            left += 1
        elif nums_sorted[left] + nums_sorted[right] > nums_sorted[i]:
            right -= 1
        else:
            count += 1
            break

print(count)
