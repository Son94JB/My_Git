import sys
input = sys.stdin.readline

A, B, D = map(int, input().split())
temp = [1]*(B+1)
for i in range(2, int(B**0.5)+1):
    if temp:
        for j in range(i+i, B+1, i):
            temp[j] = 0
prime = [i for i in range(A, B+1) if temp[i]]

cnt = 0
for x in prime:
    if str(D) in str(x):
        cnt += 1
        
print(cnt)
