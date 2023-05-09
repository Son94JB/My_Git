N = int(input())
point = N - (len(str(N))*9)
if N < (len(str(N))*9)+1:
    point = 0

for i in range(point, N):
    a = str(i)
    b = list(map(int, a))
    if sum(b) + int(a) == N:
        ans = i
        break
    else:
        ans = 0
print(ans)
