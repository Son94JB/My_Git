def toggle(a):
    if a == 0:
        return 1
    else:
        return 0


def change(idx, switches):
    switches[idx] = toggle(switches[idx])
    if idx > 0:
        switches[idx - 1] = toggle(switches[idx - 1])
    if idx < len(switches) - 1:
        switches[idx + 1] = toggle(switches[idx + 1])

    return switches


def solve(N, switch, goal):
    count1 = 0
    count2 = 1
    switch1 = switch[:]
    switch2 = switch[:]

    # 첫 번째 스위치를 누르지 않는 경우
    for i in range(1, N):
        if switch1[i - 1] != goal[i - 1]:
            switch1 = change(i, switch1)
            count1 += 1

    # 첫 번째 스위치를 누르는 경우
    switch2 = change(0, switch2)
    for i in range(1, N):
        if switch2[i - 1] != goal[i - 1]:
            switch2 = change(i, switch2)
            count2 += 1

    if switch1 == goal and switch2 != goal:
        return count1
    elif switch1 != goal and switch2 == goal:
        return count2
    elif switch1 == goal and switch2 == goal:
        return min(count1, count2)
    else:
        return -1


N = int(input())
switch = list(map(int, input()))
goal = list(map(int, input()))

print(solve(N, switch, goal))
