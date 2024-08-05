def solution(phone_book):
    answer = True
    phone_book.sort()
    # 전화번호들이 주어질 때, 한 전화번호가 다른 전화번호의 접두어인 경우가 있다면 false를 반환
    # 각 전화번호의 길이는 1 ~ 20, 전화번호부는 1 ~ 1000000
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            answer = False
            break

    return answer