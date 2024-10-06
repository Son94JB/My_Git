# 데이터는 ["코드 번호(code)", "제조일(date)", "최대 수량(maximum)", "현재 수량(remain)"]
# 으로 구성되어 있으며 현식이는 이 데이터들 중 조건을 만족하는 데이터만 뽑아서 정렬하려한다.
# data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후,
# sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return
def solution(data, ext, val_ext, sort_by):
    answer = []

    if ext == "code":
        idx = 0
    elif ext == "date":
        idx = 1
    elif ext == "maximum":
        idx = 2
    else:
        idx = 3

    if sort_by == "code":
        sorting = 0
    elif sort_by == "date":
        sorting = 1
    elif sort_by == "maximum":
        sorting = 2
    else:
        sorting = 3

    for temp in data:
        if temp[idx] < int(val_ext):
            answer.append(temp)

    answer.sort(key=lambda x:x[sorting])

    return answer