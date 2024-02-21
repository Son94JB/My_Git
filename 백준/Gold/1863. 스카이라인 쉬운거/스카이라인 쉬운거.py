n = int(input())

skylines = list()
for _ in range(n):
    skylines.append(int(input().split()[1]))
skylines.append(0)

# 고도가 이어지면 한 건물로 봐도 됨.
# 고도가 이어지지 않는다면 다른 건물
# => 건물이 낮아지면 해당 건물이 끝나는 경우
# 다만 여러 건물이 같이 끝나는 경우를 생각

stack = [0]
cnt = 0

for point in skylines:
    height = point
    while stack[-1] > point:
        if stack[-1] != stack[-2]:
            cnt += 1
            height = stack[-1]
        stack.pop()
    stack.append(point)

print(cnt)