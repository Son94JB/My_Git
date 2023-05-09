A, B = map(int, input().split())
if B < A:
    A, B = B, A
if B == A:
    ans = A
else:    
    while B % A:
        temp = B % A
        B = A
        A = temp
    ans = A
print('1' * ans)
