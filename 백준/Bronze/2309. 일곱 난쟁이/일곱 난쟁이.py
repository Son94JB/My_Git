dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
spy = sum(dwarf) - 100
f = 0
r = 8
dwarf.sort()
while True:
    if dwarf[f] + dwarf[r] == spy:
        dwarf[f] = dwarf[r] = 0
        break
    elif dwarf[f] + dwarf[r] > spy:
        r -= 1
    else:
        f += 1
dwarf.sort()
dwarf.pop(0)
dwarf.pop(0)
for i in range(7):
    print(dwarf[i])
