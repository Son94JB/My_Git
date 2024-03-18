def solution(h1, m1, s1, h2, m2, s2):
    # 시작 시간과 종료 시간 사이에서 초침이 시침이나 분침을 지나가는 횟수 계산
    temp = from_midnight(h2, m2, s2) - from_midnight(h1, m1, s1)
    
    # 시작 시간이 자정 또는 정오인 경우 예외 처리
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        temp += 1
    
    answer = temp
    
    return answer

def to_seconds(h, m, s):
    # 시간을 초 단위로 변환
    seconds = h * 3600 + m * 60 + s
    return seconds

def from_midnight(h, m, s):
    # 시침, 분침, 초침의 각도 계산
    h_angle = (h % 12 * 30 + m * 0.5 + s * (0.5 / 60)) % 360
    m_angle = (m * 6 + s * 0.1) % 360
    s_angle = s * 6
    
    ret = 0
    
    # 초침이 분침과 시침을 지나가는 경우 카운트
    if s_angle >= m_angle:
        ret += 1
    if s_angle >= h_angle:
        ret += 1
    
    # 전체 시간 동안 초침이 분침과 시침을 지나가는 횟수 계산
    ret += (h*60 + m) * 2
    ret -= h
    if h >= 12:
        ret -= 2
    
    return ret
