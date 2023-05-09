def sol(cnt):
    if cnt == M:
        print(*arr)
        return

    for i in range(N):
        if arr and arr[-1] > nums[i]:
            continue
        arr.append(nums[i])
        sol(cnt+1)
        arr.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
select = [False]*N
arr = []
sol(0)
