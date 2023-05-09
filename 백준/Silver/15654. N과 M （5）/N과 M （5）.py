def solve(cnt, nums, select):
    if cnt == M:
        print(*ans)
        return

    for i in range(N):
        if select[i]:
            continue
        select[i] = True
        ans.append(nums[i])
        solve(cnt+1, nums, select)
        ans.pop()
        select[i] = False


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
select = [False] * N
ans = []
solve(0, nums, select)