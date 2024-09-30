T = int(input())

nums = []
for i in range(T):
    n = int(input())
    nums.append(n)

nums.sort()
for n in nums:
    print(n)
