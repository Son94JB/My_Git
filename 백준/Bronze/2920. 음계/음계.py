import sys
input = sys.stdin.readline

a_cnt = 0
d_cnt = 0

note = list(map(int, input().split()))
for i in range(7):
    if note[i] < note[i+1]:
        a_cnt += 1
    else:
        d_cnt += 1

if a_cnt == 7:
    print('ascending')
elif d_cnt == 7:
    print('descending')
else:
    print('mixed')

