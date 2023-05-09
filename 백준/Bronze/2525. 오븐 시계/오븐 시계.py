h, m = map(int, input().split())
time = int(input())
finish = m + time
while finish >= 60:
    finish -= 60
    h += 1
    if h == 24:
        h = 0

m = finish
print(h, m)
