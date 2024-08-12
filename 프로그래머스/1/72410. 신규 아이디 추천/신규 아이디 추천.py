import re

def solution(new_id):
    # 1단계: 모든 대문자를 소문자로 변환
    new_id = new_id.lower()

    # 2단계: 허용되지 않는 문자 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)

    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'\.{2,}', '.', new_id)

    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')

    # 5단계: 빈 문자열일 경우 "a" 대입
    if not new_id:
        new_id = 'a'

    # 6단계: 길이가 16자 이상일 경우 처리
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')  # 끝의 마침표 제거

    # 7단계: 길이가 2자 이하일 경우 마지막 문자 반복 추가
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id