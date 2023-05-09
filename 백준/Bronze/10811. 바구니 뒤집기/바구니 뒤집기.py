N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    a = basket[s-1:e]
    a.reverse()
    basket[s-1:e] = a

print(*basket)
