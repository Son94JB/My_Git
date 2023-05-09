N = int(input())
arr = list(map(int, input().split()))
best = max(arr)
for i in range(N):
    arr[i] = (arr[i]/best) * 100

ans = sum(arr)/N
print(ans)
