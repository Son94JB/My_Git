stack = []

N = int(input())

for _ in range(N):
    command = input()
    if "push" in command:
        stack.append(int(command[5:]))

    elif command == "pop":
        if stack:
            temp = stack.pop()
            print(temp)
        else:
            print(-1)

    elif command == "size":
        print(len(stack))

    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)

    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)

